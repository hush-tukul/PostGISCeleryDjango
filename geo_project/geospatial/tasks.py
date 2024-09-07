# geo_project/geospatial/tasks.py

from celery import shared_task

@shared_task
def process_geospatial_data():
    # Your processing logic here
    return "Geospatial data processed"
