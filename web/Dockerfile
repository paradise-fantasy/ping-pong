FROM hypriot/rpi-node:7.4

RUN mkdir -p /code/web
WORKDIR /code/web

ADD package.json /code/web/
RUN npm install

ADD . /code/web/

EXPOSE 3000
CMD [ "npm", "start" ]
