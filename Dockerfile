FROM python:3.8.10-alpine

WORKDIR /flaskScanningServer
ADD . /flaskScanningServer

RUN pip install -r requirements.txt

CMD ["python", "app.py"]