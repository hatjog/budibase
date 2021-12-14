# pull official base image
FROM python:3.9-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
#RUN apt-get update \
#  && apt-get -y install netcat gcc postgresql \
#  && apt-get clean

RUN apt update && \
    apt install -y postgresql-client
RUN apt upgrade
#RUN apt add --no-cache iputils-ping
#RUN apt add --no-cache bash

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install aiofiles

# add app
COPY . .


EXPOSE 7654
