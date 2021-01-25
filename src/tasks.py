import logging
import dramatiq
from app.settings import TASKS_REDIS


# Connect to brocker
dramatiq.set_broker(RedisBroker(host=TASKS_REDIS['HOST'], port=TASKS_REDIS['PORT']))


@dramatiq.actor(actor_name='taskname', max_retries=3)
def taskname(payload: dict):
  if True:
    variable = 0
    logger.info(f'some info: {variable}')
  if False:
    payload = {}
    delay = 0
    taskname.send_with_options(args=(payload,), delay=delay)
