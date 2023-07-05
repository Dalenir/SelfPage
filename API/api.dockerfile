FROM python:3.11

ENV PYTHONUNBUFFERED=1

LABEL version = '0.1'
LABEL master = 'Neveric'

RUN mkdir /LittleAPI
WORKDIR /LittleAPI
COPY ./requirements.txt /tmp/

RUN apt-get update
RUN apt-get autoclean -y & apt-get autoremove -y

RUN pip3 install --upgrade pip
RUN pip3 install -r /tmp/requirements.txt