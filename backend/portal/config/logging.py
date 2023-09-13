import os
from pathlib import Path

'''
Дополнительная информация:
небольшой туториал
https://django.fun/ru/docs/django/4.1/topics/logging/
немного примеров
https://webdevblog.ru/loggirovanie-v-django-nachalnyj-obzor/?ysclid=lm9ny9bv8b769751273
'''

LOG_DIR = Path(__file__).resolve().parent.parent.parent.joinpath('logs')

if not os.path.isdir(LOG_DIR):
    os.mkdir(LOG_DIR)
    

# DEBUG: системная информация низкого уровня для отладки
# INFO: Общая информация о системе
# WARNING: Информация, описывающая возникшую незначительную проблему.
# ERROR: Информация, описывающая возникшую серьезную проблему.
# CRITICAL: Информация, описывающая возникшую критическую проблему.    

LOGGING = {
    'version': 1,
    # Этот параметр отключает существующие логгеры. По умолчанию Django использует некоторые из своих собственных логеров.
    'disable_existing_loggers': False,    
    
    # Определяет, как будут выглядеть строки в логгах
    'formatters': {
        # name - имя модуля
        # asctime - точное время
        # levelname - уровень
        # message - само сообщение
        # process - название процесса
        # thread - номер ядра        
        
        # Подробный вывод
        'verbose': {
            'format': ' %(asctime)-8s %(name)-8s %(levelname)-8s %(message)s',
        },
        # Упрощённый вывод
        'simple': {
            'format': '%(name)-12s %(levelname)-8s %(message)s',
        },
    },
    # Для обеспечения дополнительного контроля над тем, какие записи журнала передаются от регистратора к обработчику, используется фильтр.   
    # 'filters': {
    #     'special': {
    #         '()': 'project.logging.SpecialFilter',
    #         'foo': 'bar',
    #     },
    #     'require_debug_true': {
    #         '()': 'django.utils.log.RequireDebugTrue',
    #     },
    # },
    
    # Обработчики все опсианы тут:
    # https://docs.python.org/3/library/logging.handlers.html
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'INFO',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'verbose',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'error.log',
            'formatter': 'verbose',
        },
    },
    
    # Логеры, связываем все в систему:
    'loggers': {
        # Этот логгер обрабатывает все сообщения вызванные HTTP-запросами и вызывает исключения для определенных кодов состояния
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # Логгер общего назначения отладки
        'logfile': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'debug.log'),
            'maxBytes': 10000,
            'backupCount': 2,
        },
        # Логгер общего назначения ошибок
        'logfile_error': {
            'handlers': ['error_file'],
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'logfile_error.log'),
            'maxBytes': 10000,
            'backupCount': 2,
        },
    },
}