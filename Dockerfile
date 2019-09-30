FROM ubuntu:18.04
RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install requests
RUN pip3 install paramiko
RUN mkdir /app/
ADD src/ /app/
CMD python3 -W ignore /app/main.py