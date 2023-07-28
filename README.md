# Проект django_portal

The portal was written to develop my experience and skills

Вставить 2 ссылки: на настройку докера и сами уроки

Сборка: 
`docker-compose -f docker-compose-dev.yml build`

Монтирование контейнеров и запуск:
`docker-compose -f docker-compose-dev.yml up`

Выполнить миграцию внутри контейнера
`docker-compose -f docker-compose-dev.yml exec app python manage.py migrate --noinput`

Запустить базу данных postgres и подключиться к ней используя пароль и навзание базы данных
d`ocker-compose -f docker-compose-dev.yml exec db psql --username=postgres --dbname=django-portal-db`

# Отладка Python (в оболочке VS Code):
1.  Враинт 1
Удалённо подлючиться  к контейнеру и запутсить отладку в контейнере, однако это не практично
2. Использовать конфигурацию для удалённого подключения python "Jango Portal Python Debug" (.vscode/launch.json)
Перед этим необходимо запустить контейнеры ("docker-compose-dev.debug.yml").
Отличие в том, что в этом контейнере урезаны лишние контейнеры,  только необходимый для отладки функционал.

https://code.visualstudio.com/docs/datascience/jupyter-notebooks#_connect-to-a-remote-jupyter-server
# Отладка Jupyter (в оболочке VS Code):
1. Запустить контейнер для отладки
`docker-compose -f docker-compose-dev.debug.yml up`

скопировать URL адрес сервера jupyter
пример: http://127.0.0.1:8888/?token=9795db6df98f4246a7b353d262f6acdac7b4bff00e67d57d
перейти в требуемый испольняемый файл jupyter notebook
выбрать ядро kernel - ("Existing Jupyter Server")
указать скопированный адресс ранее
задать имя конфигурации
зпустить выполнение


Подключиться к оболчке контейнера app:
`docker exec -it django-portal-app sh`

Подключиться к порталу
http://127.0.0.1:8000

Поддключиться к отладке Jupyter:
http://127.0.0.1:8888/tree?

Подключиться к документации MkDocs:
http://localhost:8200/