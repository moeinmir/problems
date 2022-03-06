from celery.utils.log import get_task_logger

from DrfMaktab.celery import app

logger = get_task_logger(__name__)


@app.task(Bind=True)
def test_task():
    logger.info('Test task running ...')
