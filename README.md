# url_shortener_api

Restful API demonstrates URL Shortining application with Flask framework by using MVC design pattern.


Routes:
  /shorten_url              --> create a new data in db (original url, short url, redirect counter, created date)
  
  /{host}:{port}/short_url  --> redirect to original url
  
  /list_shortened_url       --> list of all data from UrlRecords db table
