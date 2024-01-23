# Интернационализация

В самом стандартом виде осуществляется средствами Django
Нужно установить gettext (apk add gettext)

[Документация](https://docs.djangoproject.com/en/4.2/topics/i18n/).

Для кастомного перевода моделей можно использовать расширение
[django-modeltranslation](https://django-modeltranslation.readthedocs.io/en/latest/)

Для перевода необходимо находить в корне приложения (manage.py), где находится папка locale (можно создать папку).
Формирует файл .po

```bush
python manage.py makemessages -l ru

```
Устанавливаем переводы.
Компилирует файл в двоичный .mo
```bush
python manage.py compilemessages
```

Для удобства можно использовать приложение для редактировать файлов с расширением .po - Poedit (свободнораспростроняемое).