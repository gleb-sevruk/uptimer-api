djangok8.settings.

briteapps_django_data => my_django_data

create set_docker_env.sh



MacOs local:
brew install rabbitmq


To have launchd start rabbitmq now and restart at login:
  brew services start rabbitmq
  brew services stop rabbitmq
Or, if you don't want/need a background service you can just run:
  rabbitmq-server