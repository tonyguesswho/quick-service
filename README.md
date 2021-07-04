# quick-service
 An app that allows customers to create service requests



$ docker-compose down -v
$ docker-compose up -d --build
$ docker-compose exec api python manage.py recreate_db
$ docker-compose exec api python manage.py seed_db

$ docker-compose exec api python -m pytest "src/tests" -p no:warnings
$ docker-compose exec api flake8 src
$ docker-compose exec api black src
$ docker-compose exec api isort src
