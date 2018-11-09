#!/usr/bin/env bash
source set_docker_env.sh

# zero downtime script
/usr/local/bin/docker-compose up --scale web=1 --no-recreate --build -d web

/usr/local/bin/docker-compose up --scale web=2 -d web
echo 'sleeping 10 secs to allow second scaled container to start'
sleep 10
docker restart deployment_web_1