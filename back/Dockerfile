FROM python:3.6.9

RUN mkdir -p /app
WORKDIR /app

ADD requirements.txt /app
RUN pip install -r requirements.txt

ADD . /app

CMD ["python", "web.py"]