# celery_config.py
from celery import Celery

redis_url = "redis://localhost:6379/0"
celery_app = Celery(
    "blood_analysis",
    broker=redis_url,
    backend=redis_url,
    include=["tasks"]
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)