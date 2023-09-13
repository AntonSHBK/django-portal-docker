# Тестирование

Файлы тестов находятся в директории `tests` соответсвующего модуля.

В свою очередь в директория тест содержит несколько исполняемых файлов, проверяющssих определённый функционал приложения.

[Документация](https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Testing) на русском, кратко описаны основы.

[Документация](https://docs.djangoproject.com/en/dev/topics/testing/#assertions) основа (Eng).

[Документация](https://docs.djangoproject.com/en/4.2/topics/testing/tools/#assertions)
 официальная (Eng).

 Запуск тестов

 ```bash
 python3 manage.py test
 python3 manage.py test catalog.tests   # Run the specified module
 python3 manage.py test catalog.tests.test_models  # Run the specified module
 python3 manage.py test catalog.tests.test_models.YourTestClass # Run the specified class
 python3 manage.py test catalog.tests.test_models.YourTestClass.test_one_plus_one_equals_two  # Run the specified method

```


