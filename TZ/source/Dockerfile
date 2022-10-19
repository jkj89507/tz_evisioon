FROM python:3.10

WORKDIR /source

COPY ./requirements.txt /source

RUN pip3 install --upgrade pip -r requirements.txt

COPY . /source

EXPOSE 5000
