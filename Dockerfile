FROM python:3-onbuild

MAINTAINER Soham Dutta
RUN git clone https://github.com/NP-compete/Job-Test-Repo.git /code
WORKDIR /code
CMD python3 main.py
