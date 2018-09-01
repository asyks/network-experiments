FROM python:3.6-alpine

WORKDIR /opt/experiments/
COPY ./requirements.txt /opt/experiments/

RUN pip install -r requirements.txt

COPY ./server /opt/experiments/
