FROM node:0.10.34-slim
MAINTAINER Pathwar Team <hacking@pathwar.net> (@pathwar_net)

RUN npm install -g pm2 grunt bower npm-check-updates
RUN mkdir /server
VOLUME ["/server"]
WORKDIR /server
EXPOSE 1337

COPY package.json /server/
RUN npm install
COPY . /server
#CMD
