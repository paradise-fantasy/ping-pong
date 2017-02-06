FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code/api
WORKDIR /code/api
ADD requirements.txt /code/api/
RUN pip install -r requirements.txt
ADD . /code/api/
