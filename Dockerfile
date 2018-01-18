FROM python:3.6.4-alpine
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt

RUN pip3 install pip --upgrade \
    && pip3 install -r /requirements.txt

EXPOSE 8080

WORKDIR /app

ADD . /app

VOLUME /app

CMD FLASK_APP=app/main.py flask run --host 0.0.0.0 --port 8080
