# django_portal

The portal was written to develop my experience and skills

Вставить 2 ссылки: на настройку докера и сами уроки

команда для билда: 
docker-compose -f docker-compose-dev.yml build

Монтирование контейнеров:
docker-compose -f docker-compose-dev.yml up

Выполнить миграцию внутри контейнера
docker-compose -f docker-compose-dev.yml exec app python manage.py migrate --noinput

Запустить базу данных postgres и подключиться к ней используя пароль и навзание базы данных
docker-compose -f docker-compose-dev.yml exec db psql --username=postgres --dbname=django-portal-db