import requests
from celery import shared_task

GEOSERVER_URL = 'http://geoserver:8080/geoserver/rest/'
GEOSERVER_USER = 'admin'
GEOSERVER_PASSWORD = 'geoserver'


@shared_task
def fetch_geoserver_workspaces():
    """
    Fetch the list of workspaces from GeoServer using the REST API.
    """
    url = f"{GEOSERVER_URL}workspaces"

    response = requests.get(url, auth=(GEOSERVER_USER, GEOSERVER_PASSWORD), headers={"Accept": "application/json"})

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch workspaces. Status code: {response.status_code}"}
