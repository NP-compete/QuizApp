FROM python:3-onbuild

MAINTAINER Soham Dutta

ADD . /code
RUN pip install -r /code/Requirements.txt
WORKDIR /code

CMD python main.py
