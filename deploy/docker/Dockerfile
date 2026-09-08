FROM python:3.14-slim

WORKDIR /python
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /python

CMD ["python3", "main.py"]

