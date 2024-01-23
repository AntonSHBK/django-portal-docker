# Индексация страниц 

Файл для индексации поисковыми системами находится `templates/portal/robots.txt`

Создать файл `robots.txt` в директории `templates` с содержанием:

```
User-agent: *
Disallow: /admin/
Disallow: /accounts/
```
Более подробно можно ознакомиться в [документации](https://django.fun/ru/articles/tutorials/kak-dobavit-robotstxt-na-svoj-sajt-django/)

Добавить urls:

```python
from django.urls import re_path
from django.views.generic import TemplateView

urlpatterns += [
    re_path(r'^robots\.txt$',
        TemplateView.as_view(template_name = 'robots.txt',
                             content_type='text/plain')),]
```

Что бы проверить работоспособность перейдите по адресу:

[http://127.0.0.1:8000/robots.txt](http://127.0.0.1:8000/robots.txt)

[Документация](https://django.fun/ru/articles/tutorials/kak-dobavit-robotstxt-na-svoj-sajt-django/)