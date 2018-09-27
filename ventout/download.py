from .celery import app


@app.task
def something():
    pass