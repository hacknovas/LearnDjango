FROM ubuntu

WORKDIR /app

COPY requirements.txt .
RUN mkdir myproject
COPY myproject /app/myproject

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip && \
    pip install -r requirements.txt

WORKDIR /app/myproject

CMD python3 manage.py runserver 0.0.0.0:8000
