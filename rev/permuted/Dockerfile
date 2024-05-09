FROM ubuntu:22.04 as build

RUN apt-get update -y; apt-get install build-essential -y
ADD main.c /tmp/permuted.c
ADD Makefile /tmp/Makefile
RUN cd /tmp/; make