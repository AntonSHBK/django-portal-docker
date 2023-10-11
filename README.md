# Мой Django проект портфолио
Проект пример. В данном проекте используюся различные технологии и методы:
- PosgresQL
- PgAdmin (ситуативно)
- Python Debug
- Jupyter
- McDocs
- Средства индексации страниц SEO (robots.txt, sitemap)
- Nginx
- Docker Compose
- Boostrap
- Celery
- Celery-Beat
- Constance


# Что нужно изучить
- Продалжить смотреть уроки Бовсуновского
- Изучить основы тестирования в pytests или тесты встроеннные в Django
- Изучить и разобраться что такое "валидатор" в Django
- Функционирование React и работа с ним
- Стили и работа в Boostrap
- Не забывать про ROS
- ~~Подумать над использованием Celer (celery-beat для админки)~~
- ~~Разобраться с логированием (хотя бы со станддартым)~~
- Написать страничку для одного поста, а также представления для редактирования и удаления
- Добавить локализацию .po
- Разобраться с модулем constance
- Сделать номрмальный интерфейс, разобраться со стилями, а лучше написать своё окно регистрацции и тд.

# Сделать сейчас:
- форму авторизации
- форму новой статьи 

## Разработка: 

Разработка: включает контейнер с функционирующим сервером Django и сервером быза данных PostgesQL.

```bash
docker-compose -f docker-compose-dev.yml build
```

```bash
docker-compose -f docker-compose-dev.yml up
```

## Разработка с отладкой в ручном режими или с испольщованием VS Code:
Разработка с отладкой в ручном режими или с испольщованием VS Code: включает контейер с севером Django, базой данных PosgresQL, сервером Jupyter.

```bash
docker-compose -f docker-compose-dev-debug.yml build
```

```bash
docker-compose -f docker-compose-dev-debug.yml up
```

## Продакшн:
Производство: включает контейнер сервер Gunicorn, базой данных PosgresQL и сервер для обратного проксирвоания Nginx.

```bash
docker-compose -f docker-compose-prod.yml build
```

```bash
docker-compose -f docker-compose-prod-debug.yml up
```

## Пояснение:
Я постарался что бы в процессе сборки не возникало проблем однако это не исключено, проблемы могут возникнуть если на одной машине будут смонитрованы разные версии контейнеров (prod, dev). Также проблемы могут быть из-за не синхронного запуска контейнеров, я предусмотерл ожидение контейнеров предд запуском, вы может изменит этот параметр (sleep 5s).

Параметры конфигурации вынесены в файл [.env](env/.env) и [db.env](env/db.env).
Зависимости python вынесены в файл [comment.txt](pip_install_txt/comment.txt) [development.txt](pip_install_txt/development.txt) и [production.txt](requirements/production.txt) .

(RUS) Если необходимы дополнительные команды при сборке образа, используйте файл  [entrypoint.sh](entrypoint.sh) и [entrypoint.prod.sh](entrypoint.prod.sh). Эти баш команды выаолянют в момент создания образа (build).


Подключиться к оболчке контейнера app:
```bash
docker exec -it django-portal-app sh
```

Подключиться к порталу
http://127.0.0.1:8000

Поддключиться к отладке Jupyter:
http://127.0.0.1:8888/tree?

Подключиться к документации MkDocs:
http://localhost:8200/

# Индексация страниц 

Файл для индексации поисковыми системами находится `templates/portal/robots.txt`

Создать файл `robots.txt` в директории `templates` с содержанием:

```
User-agent: *
Disallow: /admin/
Disallow: /accounts/
```
Более подробно можно онакомиться в [документации](https://django.fun/ru/articles/tutorials/kak-dobavit-robotstxt-na-svoj-sajt-django/)

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

# Suprvisor

[Документация](http://supervisord.org/running.html)