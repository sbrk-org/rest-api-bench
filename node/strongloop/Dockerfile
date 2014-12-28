FROM moul/strongloop:latest
MAINTAINER Pathwar Team <hack@pathwar.net> (@pathwar_net)

COPY server/package.json /server/
RUN npm install
COPY server /server
CMD ["slc", "run"]
