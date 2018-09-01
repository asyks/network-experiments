FROM python:3.6-alpine

WORKDIR /opt/client/
COPY ./requirements.txt /opt/client/

RUN pip install -r requirements.txt

COPY ./main.py /opt/client/
