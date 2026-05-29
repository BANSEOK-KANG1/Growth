(function () {
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const isCoarsePointer = window.matchMedia('(hover: none), (pointer: coarse)').matches;

  function initReveal() {
    const nodes = document.querySelectorAll('.reveal');
    if (!nodes.length) return;

    if (prefersReduced) {
      nodes.forEach((el) => el.classList.add('is-visible'));
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );

    nodes.forEach((el, index) => {
      el.style.transitionDelay = `${Math.min(index % 6, 5) * 60}ms`;
      observer.observe(el);
    });
  }

  function initCounters() {
    const counters = document.querySelectorAll('[data-count]');
    if (!counters.length || prefersReduced) return;

    const animate = (el) => {
      const target = Number(el.getAttribute('data-count'));
      const suffix = el.getAttribute('data-suffix') || '';
      const prefix = el.getAttribute('data-prefix') || '';
      const duration = 900;
      const start = performance.now();

      const tick = (now) => {
        const progress = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        const value = Math.round(target * eased);
        el.textContent = `${prefix}${value}${suffix}`;
        if (progress < 1) requestAnimationFrame(tick);
      };

      requestAnimationFrame(tick);
    };

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            animate(entry.target);
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 }
    );

    counters.forEach((el) => observer.observe(el));
  }

  function initTyping() {
    const nodes = document.querySelectorAll('[data-typing]');
    if (!nodes.length) return;

    nodes.forEach((el) => {
      let phrases = [];
      try {
        phrases = JSON.parse(el.getAttribute('data-phrases') || '[]');
      } catch {
        phrases = [];
      }
      if (!phrases.length) return;

      if (prefersReduced) {
        el.textContent = phrases[0];
        return;
      }

      let phraseIndex = 0;
      let charIndex = 0;
      let deleting = false;
      const typeSpeed = 72;
      const deleteSpeed = 38;
      const pauseEnd = 2200;
      const pauseStart = 480;

      const tick = () => {
        const current = phrases[phraseIndex];

        if (!deleting) {
          el.textContent = current.slice(0, charIndex + 1);
          charIndex += 1;

          if (charIndex === current.length) {
            deleting = true;
            setTimeout(tick, pauseEnd);
            return;
          }

          setTimeout(tick, typeSpeed + Math.random() * 28);
          return;
        }

        el.textContent = current.slice(0, charIndex - 1);
        charIndex -= 1;

        if (charIndex === 0) {
          deleting = false;
          phraseIndex = (phraseIndex + 1) % phrases.length;
          setTimeout(tick, pauseStart);
          return;
        }

        setTimeout(tick, deleteSpeed);
      };

      tick();
    });
  }

  function initMouseEffects() {
    if (prefersReduced || isCoarsePointer) return;

    const glow = document.querySelector('.fx-glow');
    const cursor = document.querySelector('.fx-cursor');
    if (!glow || !cursor) return;

    document.body.classList.add('has-mouse-fx');

    let targetX = window.innerWidth / 2;
    let targetY = window.innerHeight / 2;
    let glowX = targetX;
    let glowY = targetY;
    let cursorX = targetX;
    let cursorY = targetY;
    let rafId = 0;

    const pointerTargets = 'a, button, [role="button"], .btn-primary, .btn-secondary, .nav-cta, .case-card, input, textarea, label';

    const setTarget = (x, y) => {
      targetX = x;
      targetY = y;
    };

    const animate = () => {
      cursorX += (targetX - cursorX) * 0.28;
      cursorY += (targetY - cursorY) * 0.28;
      glowX += (targetX - glowX) * 0.08;
      glowY += (targetY - glowY) * 0.08;

      cursor.style.transform = `translate3d(${cursorX}px, ${cursorY}px, 0)`;
      glow.style.transform = `translate3d(${glowX}px, ${glowY}px, 0)`;
      rafId = requestAnimationFrame(animate);
    };

    document.addEventListener(
      'mousemove',
      (event) => {
        setTarget(event.clientX, event.clientY);
      },
      { passive: true }
    );

    document.addEventListener(
      'mouseover',
      (event) => {
        const target = event.target;
        if (!(target instanceof Element)) return;
        document.body.classList.toggle('is-pointer-hover', Boolean(target.closest(pointerTargets)));
      },
      { passive: true }
    );

    document.addEventListener('mouseleave', () => {
      document.body.classList.remove('is-pointer-hover');
    });

    rafId = requestAnimationFrame(animate);

    window.addEventListener(
      'blur',
      () => {
        cancelAnimationFrame(rafId);
      },
      { once: false }
    );
  }

  function initTilt() {
    if (prefersReduced || isCoarsePointer) return;

    const cards = document.querySelectorAll('[data-tilt]');
    if (!cards.length) return;

    cards.forEach((card) => {
      card.addEventListener('mousemove', (event) => {
        const rect = card.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width - 0.5;
        const y = (event.clientY - rect.top) / rect.height - 0.5;
        card.style.transform = `perspective(900px) rotateX(${y * -5}deg) rotateY(${x * 6}deg) translateY(-2px)`;
      });

      card.addEventListener('mouseleave', () => {
        card.style.transform = '';
      });
    });
  }

  function initMagneticButtons() {
    if (prefersReduced || isCoarsePointer) return;

    document.querySelectorAll('.btn-primary, .btn-secondary, .nav-cta').forEach((btn) => {
      btn.addEventListener('mousemove', (event) => {
        const rect = btn.getBoundingClientRect();
        const x = event.clientX - rect.left - rect.width / 2;
        const y = event.clientY - rect.top - rect.height / 2;
        btn.style.transform = `translate(${x * 0.12}px, ${y * 0.18}px)`;
      });

      btn.addEventListener('mouseleave', () => {
        btn.style.transform = '';
      });
    });
  }

  function initToolTabs() {
    document.querySelectorAll('[data-tool-tabs]').forEach((root) => {
      const tabs = root.querySelectorAll('[data-tool-tab]');
      const panels = root.querySelectorAll('[data-tool-panel]');

      tabs.forEach((tab) => {
        tab.addEventListener('click', () => {
          const id = tab.getAttribute('data-tool-tab');
          tabs.forEach((t) => t.classList.toggle('is-active', t === tab));
          panels.forEach((panel) => {
            panel.classList.toggle('is-active', panel.getAttribute('data-tool-panel') === id);
          });
        });
      });
    });
  }

  function initYouTubeDemo() {
    document.querySelectorAll('[data-yt-demo]').forEach((root) => {
      const tabs = root.querySelectorAll('[data-tab]');
      const panels = root.querySelectorAll('[data-panel]');

      tabs.forEach((tab) => {
        tab.addEventListener('click', () => {
          const id = tab.getAttribute('data-tab');
          tabs.forEach((t) => t.classList.toggle('is-active', t === tab));
          panels.forEach((panel) => {
            const show = panel.getAttribute('data-panel') === id;
            panel.hidden = !show;
          });
        });
      });

      root.querySelectorAll('[data-format]').forEach((chip) => {
        chip.addEventListener('click', () => {
          root.querySelectorAll('[data-format]').forEach((c) => {
            c.classList.toggle('is-active', c === chip);
          });
          const fmt = chip.getAttribute('data-format');
          const shorts = root.querySelector('[data-kpi="shorts"]');
          if (shorts) {
            shorts.textContent = fmt === 'shorts' ? '71%' : fmt === 'long' ? '12%' : '38%';
          }
        });
      });

      const refreshBtn = root.querySelector('[data-yt-refresh]');
      if (refreshBtn) {
        refreshBtn.addEventListener('click', () => {
          refreshBtn.classList.add('is-spinning');
          setTimeout(() => refreshBtn.classList.remove('is-spinning'), 700);
        });
      }
    });
  }

  function initMetaDemo() {
    document.querySelectorAll('[data-meta-demo]').forEach((root) => {
      const tabs = root.querySelectorAll('[data-meta-tab]');
      const panels = root.querySelectorAll('[data-meta-panel]');

      tabs.forEach((tab) => {
        tab.addEventListener('click', () => {
          const id = tab.getAttribute('data-meta-tab');
          tabs.forEach((t) => t.classList.toggle('is-active', t === tab));
          panels.forEach((panel) => {
            const show = panel.getAttribute('data-meta-panel') === id;
            panel.hidden = !show;
          });
        });
      });

      root.querySelectorAll('[data-meta-format]').forEach((chip) => {
        chip.addEventListener('click', () => {
          root.querySelectorAll('[data-meta-format]').forEach((c) => {
            c.classList.toggle('is-active', c === chip);
          });
          const fmt = chip.getAttribute('data-meta-format');
          const videoKpi = root.querySelector('[data-meta-kpi="video"]');
          if (videoKpi) {
            videoKpi.textContent = fmt === 'video' ? '100%' : fmt === 'static' ? '25%' : '50%';
          }
        });
      });
    });
  }

  function initTheme() {
    const toggle = document.querySelector('[data-theme-toggle]');
    if (!toggle) return;

    const meta = document.querySelector('meta[data-theme-color]');
    const lightColor = '#2457c5';
    const darkColor = '#0f1729';

    const applyTheme = (theme) => {
      document.documentElement.setAttribute('data-theme', theme);
      localStorage.setItem('theme', theme);
      if (meta) meta.setAttribute('content', theme === 'dark' ? darkColor : lightColor);
    };

    toggle.addEventListener('click', () => {
      const next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      applyTheme(next);
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initReveal();
    initCounters();
    initTyping();
    initMouseEffects();
    initTilt();
    initMagneticButtons();
    initToolTabs();
    initYouTubeDemo();
    initMetaDemo();
  });
})();
