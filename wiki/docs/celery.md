# Celery

[Документация](https://docs.celeryq.dev/en/stable/index.html)

[Туториал](https://django.fun/ru/articles/tutorials/obrabotka-periodicheskih-zadach-v-django-s-pomoshyu-celery-i-docker/)


Планировщик задач использую в связке с [supervisor](supervisor.md) и брокером Redis.

Celery — это распределенная очередь задач, которая может собирать, записывать, планировать и выполнять задачи вне вашей основной программы.

Настройки celery находят в `portal/celery.py`, настройки параметров Redis `portal/config/redis.py`.

```python
# Сначала мы устанавливаем значение по умолчанию для переменной окружения DJANGO_SETTINGS_MODULE, чтобы Celery знал, как найти проект Django.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal.settings')
# Затем мы создали новый экземпляр Celery с именем core и присвоили значение переменной с именем app.
app = Celery('portal')
# Затем мы загрузили значения конфигурации celery из объекта settings из django.conf. Мы использовали namespace="CELERY", чтобы предотвратить конфликты с другими настройками Django. Другими словами, все настройки конфигурации для Celery должны иметь префикс CELERY_.
app.config_from_object('django.conf:settings', namespace="CELERY")
# Наконец, app.autodiscover_tasks() сообщает Celery искать задачи Celery из приложений, определенных в настройках.УСТАНОВЛЕННЫЕ ПРИЛОЖЕНИЯ.
app.autodiscover_tasks()

app.conf.update(
    BROKER_URL=getattr(settings, 'BROKER_URL', 'redis://redis:6379'),
    CELERY_RESULT_BACKEND=getattr(settings, 'CELERY_RESULT_BACKEND', 'redis://redis:6379'),
    CELERY_TIMEZONE='Europe/Moscow',
)
```
Параметры Redis подгружаются непосредственно в `setting.py`.

Добавил так же в `portal/__init__.py`
```python
from .celery import app as celery_app

__all__ = ("celery_app",)
```

Что бы `Celery`заработал как требуется (с использованием `django-celery-beat`) необходимо заупстить:
```
celery -A portal beat -l info --scheduler
```