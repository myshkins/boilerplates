# syntax=docker/dockerfile:1

FROM python:3.10.8-slim-buster

WORKDIR /api

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# CMD [ "python", "wsgi.py"]