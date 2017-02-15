FROM resin/raspberrypi-python:2.7

# Install OS requirements
RUN apt-get update \
    && apt-get install -yq \
        build-essential \
        cmake \
        python2.7-dev \
        unzip \
        wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

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

