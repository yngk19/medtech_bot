FROM python:3.9-slim as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update 

COPY requirements.txt .

RUN pip install -r requirements.txt

FROM python:3.9-slim

WORKDIR /app

COPY . .


CMD ["python3", "src/main.py"]


