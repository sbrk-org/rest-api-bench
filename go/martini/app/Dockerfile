FROM golang:1.4.0

ENV CGO_ENABLED 0
RUN go get github.com/tools/godep
RUN go install -a std

MAINTAINER Manfred Touron <m@42.am> (@moul)

ENV APP_DIR /go

COPY . /go/
RUN cd $APP_DIR && godep go run -a -v -ldflags '-d -w -s'

## old way
# RUN mkdir -p /go/src/app
# WORKDIR /go/src/app
# COPY . /go/src/app
# RUN go-wrapper download
# RUN go-wrapper install
# CMD go-wrapper run
