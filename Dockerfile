FROM python:3.11-slim

WORKDIR /app

COPY req.txt .

RUN pip install --no-cache-dir -r req.txt

COPY . .

RUN chmod +x start.sh

EXPOSE 8501
EXPOSE 8000

CMD ["./start.sh"]
