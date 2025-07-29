# trigger build
# trigger build
# retry push
# retry push
# retry push
# retry push
# test login fix
# Project Overview
Book Catalog API is a Django REST application that allows users to manage a collection of books through a RESTful interface. It supports listing, creating, updating, and deleting books. The project is containerized using Docker and deployed using Kubernetes with Helm. It demonstrates a full DevOps CI/CD pipeline using GitHub Actions.

# API Usage Examples
curl [http://localhost:8000/api/books/](http://localhost:8000/api/books/)

curl -X POST -H "Content-Type: application/json" \
  -d '{"title": "My Book", "author": "Zakaria", "price": 29.99}' \
  [http://localhost:8000/api/books/](http://localhost:8000/api/books/).
  
# Local Build and Run Instructions
Using Python:
git clone https://github.com/HOUSSAT99/book-catalog-api.git
cd book-catalog-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Using Docker:
docker-compose up --build

# CI/CD Pipeline Explanation
The CI/CD pipeline is triggered when changes are pushed to the master branch. It performs the following steps:

Install Python and dependencies
Run unit tests
Build a Docker image of the app
Push the image to Docker Hub
Deploy the application to Kubernetes using Helm

# Kubernetes and Helm Setup Instructions
#Start a local Kubernetes cluster
minikube start

#Deploy the app using Helm
helm install book-catalog ./helm/book-catalog

#Check deployment
kubectl get pods

#Port forward to access the API
kubectl port-forward deployment/book-catalog-deployment 8000:8000
