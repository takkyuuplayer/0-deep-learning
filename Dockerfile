FROM continuumio/anaconda3

ENV LC_ALL C

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y python-qt4
