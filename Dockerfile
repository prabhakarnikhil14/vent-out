FROM python:3.6-alpine

RUN adduser -D ventout

WORKDIR /home/ventout

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY ventout ventout
COPY run.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP run.py

RUN chown -R ventout:ventout ./
USER ventout

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
