FROM python:3.14-slim

WORKDIR App

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ['python', 'server.py']