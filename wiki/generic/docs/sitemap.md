# Карта сайта
Динамичсекая карта сайта для поисковых  сервисов, создана на базе встроенного функционала "из коробки" Django4 4.2

## Основное:
Добавить в INSTALD_APPS:
```
...
django.contrib.sites
django.contrib.sitemaps
```
 
Создать файл sitemaps.py (я создал в корневом катологе portal, но это необязательно) с содержанием примерно:

```python
from django.contrib.sitemaps import Sitemap
from blog.models import Post


class PortalSitemap(Sitemap):
    changefreq = "weekly" # переодичность проверки
    priority = 0.9 # приоритет

    def items(self): # объекты, лучше конечно обратиться к документации
        return Post.objects.all()

    def lastmod(self, obj):
        # if  object have pub_date
        return obj.date_created
```

Настроить urls:
```python
from django.urls import re_path
from django.contrib.sitemaps.views import sitemap

from .sitemaps import PortalSitemap
  
sitemaps = {'exhibist': PortalSitemap}
urlpatterns += [
    re_path(r'^sitemap\.xml$',
            sitemap, {'sitemaps': sitemaps},
            name='django.contrib.sitemaps.views.sitemap'),]

```
Убедитесь что у рассматриваемых моделей корректно задан `get_absolute_url()` (я долго провозился в поисках ошибок).

Что бы проверить работоспособность перейдите по адресу:

[http://127.0.0.1:8000/sitemap.xml](http://127.0.0.1:8000/sitemap.xml)

[Документация](https://docs.djangoproject.com/en/4.2/ref/contrib/sitemaps/)

[Видео](https://www.youtube.com/watch?v=Y0qKYFZDlmo&t=379s)