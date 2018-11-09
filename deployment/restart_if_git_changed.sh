#!/usr/bin/env bash

git fetch --all

if [[ $(git rev-parse HEAD) == $(git rev-parse @{u}) ]]; then
    echo 'remote branch has no changes, update will be skipped'
    exit
fi

git reset --hard

git pull
echo 'Found new code on remote branch.. Restarting containers'
source set_docker_env.sh
bash ./restart.sh

