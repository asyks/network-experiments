FROM python:3.6

WORKDIR /opt/server/
COPY ./requirements.txt /opt/server/

RUN pip install -r requirements.txt

COPY ./main.py /opt/server/
