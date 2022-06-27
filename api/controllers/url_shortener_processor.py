from ..models import UrlRecords, Session
import string
from random import choices
import os

host = os.getenv('FLASK_RUN_HOST')
port = os.getenv('FLASK_RUN_PORT')

session = Session()


def url_shortener_processor(original_url):
    short_url = generate_short_url()
    unique_control = session.query(UrlRecords).filter_by(original_url=original_url).first()
    if not unique_control:
        url = UrlRecords(original_url=original_url, short_url=short_url)
        session.add(url)
        session.commit()
        short_url = url.short_url
    else:
        short_url = unique_control.short_url

    return f'http://{host}:{port}/{short_url}'


def generate_short_url():
    characters_in_short_url = string.ascii_letters + string.digits
    short_url = ''.join(choices(characters_in_short_url, k=5))

    unique_control = session.query(UrlRecords).filter_by(short_url=short_url).first()
    if unique_control:
        return generate_short_url()

    return short_url
