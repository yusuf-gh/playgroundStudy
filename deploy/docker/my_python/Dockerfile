FROM python:3.14-slim
WORKDIR /python
EXPOSE 8001

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /python

CMD ["python", "main.py"]





