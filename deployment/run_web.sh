#!/bin/bash

sleep 3
echo 'Running... run.sh'
pip install -r requirements.txt
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

env
# python manage.py runserver 0.0.0.0:8080

/usr/bin/supervisord -c /code/deployment/apps-configs/supervisor-vps.conf

# if [ "$DJANGO_SETTINGS_MODULE" = "djangok8.settings.local" ]
#then
#  python manage.py runserver 0.0.0.0:8080
#else
#  /usr/bin/supervisord -c /code/deployment/apps-configs/supervisor-vps.conf
#fi
