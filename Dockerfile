FROM python:3-alpine3.18

LABEL authors="siddhant vijay singh"

WORKDIR /app

ADD . /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python ./run.py
