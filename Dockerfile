FROM python:latest
WORKDIR /iКРИТ
COPY /requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip install -r /requirements.txt
COPY . /iКРИТ

