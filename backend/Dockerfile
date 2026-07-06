FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUNN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]

