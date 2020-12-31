# pull official base image
FROM python:3.8

RUN mkdir /app
# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt-get update && \
    apt-get install -y \
        apt-utils \
        git \
        postgresql postgresql-contrib \
        python3-dev \
        musl-dev \
        gcc \
        gettext \
        swig \
        jpegoptim \
        supervisor

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . /app