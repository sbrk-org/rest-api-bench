FROM node:0.10.33-slim

RUN npm install -g sails@0.10.5

RUN mkdir /server

WORKDIR /server

ADD server/package.json /server/package.json

RUN npm install

ADD server /server

EXPOSE 1337

CMD sails lift --dev