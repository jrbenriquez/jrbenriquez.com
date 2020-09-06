# pull official base image
FROM python:3.8.5-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get -y update \
    && apt-get -y install gcc python3 musl

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt

# copy project
COPY . .
RUN pip install -r requirements.txt

CMD python manage.py migrate
