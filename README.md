# url_shortener_api

Restful API demonstrates URL Shortining application with Flask framework by using MVC design pattern.


Routes:

  /shorten_url              --> create a new data in db (original url, short url, redirect counter, created date)
  
  /{host}:{port}/short_url  --> redirect to original url
  
  /list_shortened_url       --> list of all data from UrlRecords db table 
  
  
 Containerizing steps with Kubernetes:
 
 1- create Dockerfile
 2- $ docker build -t url-shortener-api
 --> first login to dockerhub 
 3- $ docker push mustafalaca/url-shortener-api
 4- create deployment.yaml file
 5- $ kubectl apply -f deployment.yaml
 6- $ kubectl get services and kubectl deployments
 8- If you wish, you can check it on your minikube dashboard


