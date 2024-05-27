FROM python:3

WORKDIR /home

RUN apt-get update
RUN pip install --upgrade pip
COPY ./requirements.txt  /home
RUN pip install -r requirements.txt

WORKDIR /home/src

COPY ./src /home/src/
CMD [ "python", "/home/src/record_data.py" ] 