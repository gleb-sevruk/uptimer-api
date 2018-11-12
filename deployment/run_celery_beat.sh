#!/bin/bash

# wait for RabbitMQ server to start

# sleep 1
echo 'Running... run_celery_beat.sh'
celery beat -A djangok8