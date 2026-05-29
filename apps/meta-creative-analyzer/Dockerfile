FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY data ./data
COPY src ./src
COPY start.sh .
RUN chmod +x start.sh

EXPOSE 8501

CMD ["./start.sh"]
