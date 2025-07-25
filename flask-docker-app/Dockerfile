FROM python:3.10-slim

WORKDIR /app

# Install net-tools (for netstat) or iproute2 (for ss)
RUN apt update && apt install -y net-tools iproute2

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]


