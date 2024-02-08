# Dockerfile to build a flask app
FROM python:3.9.18

WORKDIR /usr/app

COPY requirements.txt . 

RUN pip install -r requirements.txt

EXPOSE 8080

COPY app.py .

CMD ["python", "app.py"]