FROM python:3.8.10

WORKDIR url_shortener_api

COPY . .

RUN pip install -r requirements.txt

CMD ["flask", "run"]
