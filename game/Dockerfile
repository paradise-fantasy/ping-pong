#FROM resin/raspberrypi-python:2.7
FROM resin/rpi-raspbian:latest

RUN apt-get update && apt-get install -y \
	build-essential \
	gcc \
	python2 \
	python2-dev \
	python2-pip \
	python2-virtualenv \
	--no-install-recommends && \
	rm -rf /var/lib/apt/lists/*


RUN mkdir -p /code/game
WORKDIR /code/game
ADD requirements.txt /code/game/
RUN pip install -r requirements.txt
ADD . /code/game/

EXPOSE 5000

CMD ["python", "main.py"]
