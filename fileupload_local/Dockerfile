FROM python:3.7.0-alpine3.8
WORKDIR /opt/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD python webapp.py
