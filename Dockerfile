FROM python:3.9-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update 

COPY . .

RUN pip install -r requirements.txt


CMD ["python3", "src/main.py"]


