from sqlalchemy import Column, Integer, String, DateTime
from . import Base
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

from . import Session

session = Session()


class UrlRecords(Base, SerializerMixin):
    __tablename__ = 'UrlRecords'
    id = Column(Integer, primary_key=True)
    original_url = Column(String(512))
    short_url = Column(String(5), unique=True)
    usage_counter = Column(Integer, default=0)
    created_date = Column(DateTime, default=datetime.now())

    def __init__(self, original_url, short_url):
        self.original_url = original_url
        self.short_url = short_url
