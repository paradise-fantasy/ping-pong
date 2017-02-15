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

# Install rest of requirements
COPY requirements.txt /code/game/
RUN pip install -r requirements.txt

# Get source code
COPY . /code/game/

# Need this for eventlet D:
COPY etc.protocols /etc/protocols

EXPOSE 5000
CMD ["python", "main.py"]
