#!/bin/bash

# wait for RabbitMQ server to start

# sleep 10
echo 'Running... run_celery.sh'
celery worker -A djangok8