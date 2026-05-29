(function () {
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

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

  document.addEventListener('DOMContentLoaded', () => {
    initReveal();
    initCounters();
    initToolTabs();
    initYouTubeDemo();
  });
})();
