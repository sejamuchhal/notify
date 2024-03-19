FROM python:3.11

WORKDIR /root/app/

ENV PYTHONDONTWRITEBYTECODE 1

COPY src/requirements.txt /root/app/

RUN pip3 install -r ./requirements.txt --no-cache-dir

ADD src/ /root/app/

RUN pip install -r  ./requirements.txt

COPY . .
