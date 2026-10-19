FROM python:3.14

WORKDIR App

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "server.py"]