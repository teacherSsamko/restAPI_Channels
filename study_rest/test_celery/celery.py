from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',
             broker='amqp://ssamko:ssamko123@localhost/ssamko_host',
             backend='rpc://',
             include=['test_celery.tasks'])


app = Celery('test_celery',
             broker='amqp://upscale-consumer:Gdflab!dev@consumer@localhost/upscale-host',
             backend='rpc://',
             include=['test_celery.tasks'])