FROM frolvlad/alpine-python3

MAINTAINER Soham Dutta
ADD . /code
RUN pip install -r /code/requirements.txt
