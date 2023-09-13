# Build and run

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

# Проект django_portal

Сборка: 
`docker-compose -f docker-compose-dev.yml build`

Монтирование контейнеров и запуск:
`docker-compose -f docker-compose-dev.yml up`

Если при запуске возникли ошибки, возможно это связано с первым запуском а так же нарушена очередность запуска, я не смог реализовать запуск одного контейнера после готовности к работе другого. Решением может быть запуск только контейнера app, web и bd, после успешного запуска уже пробовать запускать остальные.

Выполнить миграцию внутри контейнера
`docker-compose -f docker-compose-dev.yml exec app python manage.py migrate --noinput`

Запустить базу данных postgres и подключиться к ней используя пароль и навзание базы данных
d`ocker-compose -f docker-compose-dev.yml exec db psql --username=postgres --dbname=django-portal-db`

# Отладка Python (в оболочке VS Code):
1.  Враинт 1
Удалённо подлючиться  к контейнеру и запутсить отладку в контейнере, однако это не практично
2. Вариант 2. 
Использовать конфигурацию для удалённого подключения python "Jango Portal Python Debug" (.vscode/launch.json)
Перед этим необходимо запустить контейнеры ("docker-compose-dev.debug.yml").
Отличие в том, что в этом контейнере урезаны лишние контейнеры,  только необходимый для отладки функционал.

https://code.visualstudio.com/docs/datascience/jupyter-notebooks#_connect-to-a-remote-jupyter-server
# Отладка Jupyter (в оболочке VS Code):
1. Запустить контейнер для отладки, дождаться выполнения миграций. Обязательно необходимо выполнить запуск в режиме отладки (Python) шаги выше и тогда появится окно с собщение о запуске сервера. 

`docker-compose -f docker-compose-dev.debug.yml build`

`docker-compose -f docker-compose-dev.debug.yml up`

если используется токен скопировать URL адрес сервера jupyter
пример: http://127.0.0.1:8888/?token=9795db6df98f4246a7b353d262f6acdac7b4bff00e67d57d
перейти в требуемый испольняемый файл jupyter notebook
выбрать ядро kernel - ("Existing Jupyter Server")
указать скопированный адресс ранее
задать имя конфигурации
зпустить выполнение

# Важные ссылки

Подключиться к оболчке контейнера app:
`docker exec -it django-portal-app sh`

Подключиться к порталу
http://127.0.0.1:8000

Поддключиться к отладке Jupyter:
http://127.0.0.1:8888/tree?

Подключиться к документации MkDocs:
http://localhost:8200/

Создать супераользователя
python manage.py createsuperuser

Посмотреть логи контейнера для отлова ошибок
docker-compose -f docker-compose.prod.yml logs -f

Для запуска в проде
http://127.0.0.1:8000/

Создать суперпользователя
`python manage.py createsuperuser`

`python manage.py collectstatic --noinput`
`python manage.py makemigrations`
`python manage.py migrate`