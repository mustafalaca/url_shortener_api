FROM python:3.8.10

WORKDIR url_shortener_api

COPY . .

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 -e FLASK_ENV=development wsgi:app
