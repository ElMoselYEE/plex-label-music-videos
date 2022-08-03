FROM python:3.8

COPY requirements.txt .
COPY run.py .

RUN pip install -r requirements.txt

CMD python3 run.py