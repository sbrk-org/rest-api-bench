NAME =	strongloop

build:
	fig build

up:	build
	fig up -d
	fig logs

shell:	build
	fig run $(NAME) /bin/bash

console:	build
	fig run $(NAME) sails console
