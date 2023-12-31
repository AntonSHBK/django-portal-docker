# Suprvisor

[Документация](http://supervisord.org/running.html)

[Туториал](https://www.8host.com/blog/ustanovka-i-upravlenie-supervisor-na-servere-ubuntu-i-debian/?ysclid=lmiyi6wak475505912)

Supervisor – это менеджер процессов, который существенно упрощает управление долго работающими программами, предоставляя простой и понятный интерфейс.

Установка через пакетный менедер:
```
pip install supervisor
```

## Простой пример
Конфигурационный файл программы находится по адресу `/etc/supervisor/supervisord.conf.` Здесь находятся основные настройки.

Общий вид:

```properties
[program:portal]
command=celery -A portal beat -l info --scheduler 
directory = /app
user = root
autostart=true
autorestart=true
stderr_logfile=/var/log/my_comand.err.log
stderr_logfile_maxbytes = 10MB
stdout_logfile=/var/log/my_comand.out.log
stdout_logfile_maxbytes = 10MB
```
Директории указанные для  логирования должны быть предварительно созданы.
## Опция autorestart
- false – Supervisor никогда не будет перезапускать программу после завершения ее работы;
- true – Supervisor будет всегда перезапускать программу после завершения работы;
- unexpected – Supervisor будет перезапускать программу только в случае, если она завершила работу из-за возникновения неожиданного кода ошибки (любой стандартный код, кроме 0 и 2).

## Параметры

Для каждого процесса минимально надо передать такие переменные для того чтобы он автоматически запускался и восстанавливался после падения:

- directory - рабочая директория;
command - команда запуска процесса;
- user - пользователь, от имени которого будет запущен процесс;
- autostart - нужно ли автоматически запускать процесс;
- autorestart - нужно ли перезапускать процесс;
- priority - приоритет запускаемого процесса;
- environment - переменные окружения, которые надо передать процессу;
- stdout_logfile - куда перенаправлять вывод stdout процесса;
- stderr_logfile - куда перенаправлять вывод stderr процесса;
- process_name - название процесса, с возможностью подстановки номера копии (`process_name=%(program_name)s_%(process_num)02d`);
- numprocs - количество запускаемых копий процесса;
- startretries - количество попыток запустить программу;
- redirect_stderr - перенаправить вывод ошибок процесса в вывод supervisor;
redirect_stdout - перенаправить вывод процесса в вывод supervisor.

Создав конфигурационный файл, нужно известить Supervisor о появлении новой программы; для этого используется команда `supervisorctl`. 
Все исполняемые программы должны находиться в этом файле. Если возникает ошибка добро пожаловать в документацию. 

```bush
supervisord -c /etc/supervisor/supervisord.conf 
supervisorctl reread
supervisorctl update
supervisorctl start all
supervisorctl status
```
Примечниение: чтобы эти изменения вступили в силу, всегда необходимо запускать две вышеперечисленные команды после редактирования любого конфигурационного файла программы.

## Управление программами
Включить интерактивный режим, запустите supervisorctl без аргументов:
```
supervisorctl
```
Посмотреть список команд:
```
help
```
Принцип действия в интерактивном режиме:
```
<назваание команды> <название выполняемого сервиса>
```
Принцип действия в обычном режиме:
```
supervisorctl <назваание команды> <название выполняемого сервиса>
```
## Полезные команды
Перезагрузить
```
supervisorctl reload
```