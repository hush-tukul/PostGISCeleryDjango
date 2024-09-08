# Building & Deployment Guide

## Prerequisites

- **Version Control**: Ensure code is committed to the repository.
- **Dependencies**: List in `requirements.txt` or similar.
- **Access**: Necessary permissions for deployment.


## IMPORTANT!!!
- **Environment variables**: Create your own .env file and fill all variables. Use .envdist as example

## Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/hush-tukul/PostGISCeleryDjango.git
    cd PostGISCeleryDjango
    ```


4. **Build and Run Docker Containers**:
    ```bash
    docker-compose up --build
    ```

## Database Setup

1. **Create Superuser**:
    ```bash
    docker-compose exec web python geo_project/manage.py createsuperuser
    ```
2. **Login in admin page**:
   ```bash
   http://localhost:8000/admin/login/
   ```

**Now you can use swagger page**:
      ```
      http://localhost:8000/swagger/
      ```


OPTIONAL
3. **Make Migrations**:
    ```bash
    docker-compose exec web python geo_project/manage.py makemigrations
    ```

4. **Apply Migrations**:
    ```bash
    docker-compose exec web python geo_project/manage.py migrate
    ```

## Deployment

### Staging

1. **Deploy to Staging**:
    ```bash
    docker-compose up -d
    ```

## Rollback

1. **Rollback Deployment**:
    ```bash
    docker-compose down
    ```

## Background tasks checking
After ```docker-compose up --build``` put ```docker-compose exec web python geo_project/manage.py shell```
And after: 
```
from geospatial.tasks import fetch_geoserver_workspaces
result = fetch_geoserver_workspaces.delay()
result.get(timeout=10)
```
If return is like below, everything is fine:
```{'workspaces': {'workspace': [{'name': 'cite', 'href': 'http://geoserver:8080/geoserver/rest/workspaces/cite.json'}, {'name': 'it.geosolutions', 'href': 'http://geoserver:8080/geoserver/rest/workspaces/it.geosolutions.json'}, {'name': 'ne', 'href': 'http://geoserver:8080/geoserver/rest/workspaces/ne.json'}, {'name': 'nurc', 'href': 'http://geoserver:8080/geoserver/rest/workspaces/nurc.json'}, {'name': 'sde', 'href': 'http://geoserver:8080/geoserver/rest/workspaces/sde.json'}, {'name': 'sf', 'href': 'http://geoserver:8080/geoserver/rest/workspaces/sf.json'}, {'name': 'tiger', 'href': 'http://geoserver:8080/geoserver/rest/workspaces/tiger.json'}, {'name': 'topp', 'href': 'http://geoserver:8080/geoserver/rest/workspaces/topp.json'}]}}
```
To exit the IntercativeConsole use Ctrl+D
