FROM python:3-onbuild

MAINTAINER Soham Dutta
ADD . /code/
WORKDIR /code
CMD python3 main.py
