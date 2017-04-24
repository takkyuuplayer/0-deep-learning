DOCKER=$(shell which docker)

build:
	$(DOCKER) build 0-deep-learning .
up:
	$(DOCKER) run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix${DISPLAY} -i -t 0-deep-learning /bin/bash

up/notebook:
	$(DOCKER) run -i -t -p 8888:8888 0-deep-learning \
		/bin/bash -c "/opt/conda/bin/conda install jupyter -y --quiet &&\
		mkdir /opt/notebooks && /opt/conda/bin/jupyter notebook \
		--notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser"

