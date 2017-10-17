FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY . /code/

RUN apt-get update -qq
RUN apt-get install -y libblas-dev liblapack-dev liblapacke-dev gfortran
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
