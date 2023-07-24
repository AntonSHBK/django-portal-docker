# Проект django_portal

The portal was written to develop my experience and skills

Вставить 2 ссылки: на настройку докера и сами уроки

Сборка: 
docker-compose -f docker-compose-dev.yml build

Монтирование контейнеров и запуск:
docker-compose -f docker-compose-dev.yml up

Выполнить миграцию внутри контейнера
docker-compose -f docker-compose-dev.yml exec app python manage.py migrate --noinput

Запустить базу данных postgres и подключиться к ней используя пароль и навзание базы данных
docker-compose -f docker-compose-dev.yml exec db psql --username=postgres --dbname=django-portal-db

Подключиться к оболчке контейнера app
docker exec -it django-portal-app sh

docker-compose -f docker-compose-dev.yml exec django_portal-jupyter-1 python manage.py shell_plus --notebook
