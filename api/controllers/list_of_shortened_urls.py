from ..models import *

session = Session()


def list_of_urls_processor():
    all_data = session.query(UrlRecords).all()
    all_data_list = list()
    for index in all_data:
        all_data_list.append(index.to_dict())

    return all_data_list
