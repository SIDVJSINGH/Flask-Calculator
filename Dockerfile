FROM python:3-alpine3.18
# FROM alpine:latest

LABEL authors="siddhant vijay singh"

# To set the timezone of the Docker container to Asia/Kolkata
RUN apk --no-cache add tzdata
ENV TZ=Asia/Kolkata

WORKDIR /app

ADD . /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python ./run.py
