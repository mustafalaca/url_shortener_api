from ..models import *

session = Session()


def redirect_to_domain(short_url):
    url = session.query(UrlRecords).filter_by(short_url=short_url).first()
    if url is None:
        return False
    url.usage_counter = url.usage_counter + 1
    session.commit()
    return url.original_url
