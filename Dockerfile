FROM python:3.7-slim as builder
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

FROM builder
CMD ["python", "main.py"]
