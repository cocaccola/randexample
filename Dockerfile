FROM python:3.8.4-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY wrapper.sh ./
COPY *.py ./

ENTRYPOINT ["./wrapper.sh"]
