FROM resin/rpi-raspbian:jessie
RUN apt-get update && apt-get install -y \
python2.7 \
python2.7-dev \
python2.7-pip \
python2.7-virtualenv

RUN mkdir -p /code/game
WORKDIR /code/game
ADD requirements.txt /code/game/
RUN pip install -r requirements.txt
ADD . /code/game/

EXPOSE 5000

CMD ["python", "main.py"]
