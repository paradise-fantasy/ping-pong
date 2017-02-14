FROM resin/raspberrypi-python:2.7
RUN mkdir -p /code/game
WORKDIR /code/game

# Cache gevent (it's soo big)
RUN pip install gevent

# Install rest of requirements
ADD requirements.txt /code/game/
RUN pip install -r requirements.txt

# Get source code
ADD . /code/game/

EXPOSE 5000

CMD ["python", "main.py"]

