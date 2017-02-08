FROM resin/raspberrypi-python:2.7
RUN mkdir -p /code/game
WORKDIR /code/game
ADD requirements.txt /code/game/
RUN pip install -r requirements.txt
ADD . /code/game/

EXPOSE 5000
