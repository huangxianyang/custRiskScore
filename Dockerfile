FROM tiangolo/uvicorn-gunicorn-fastapi:python:3.8

EXPOSE 8005/tcp

WORKDIR /modelapi

COPY ./app  modelapi/app
COPY ./conf  modelapi/conf
COPY ./scripts  scripts
COPY ./utils  utils

RUN pip install gunicorn && pip install --no-cache-dir -r requirements.txt