import os
from django.conf import settings
from celery import Celery

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
    # CELERY_DEFAULT_QUEUE=settings.CELERY_DEFAULT_QUEUE,
    # CELERY_TASK_SERIALIZER='json',
    # CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    # CELERY_RESULT_SERIALIZER='json',
    # CELERY_BEAT_SCHEDULER='django_celery_beat.schedulers:DatabaseScheduler',
    CELERY_TIMEZONE='Europe/Moscow',
    # CELERY_SEND_EVENTS=True,
    # CELERY_ENABLE_UTC=True,
    # CELERY_IGNORE_RESULT=False
)


# Tasks
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task(name='My_task')
def sample_task():
    print('lol')