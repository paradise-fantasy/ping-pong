FROM resin/raspberrypi-python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code/api
WORKDIR /code/api
COPY requirements.txt /code/api/
RUN pip install -r requirements.txt
COPY . /code/api/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
