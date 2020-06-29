FROM ubuntu:16.04

MAINTAINER I Gusti Bagus A

ADD ./stock.py /
ADD ./server.py /
ADD ./python_requirements.txt /

RUN apt -y update &&\
    apt -y install python3 python3-pip &&\
    python3 -m pip install --upgrade pip &&\
    python3 -m pip install -r python_requirements.txt

CMD [ "python3", "-u", "./server.py" ]
