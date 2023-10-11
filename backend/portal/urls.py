# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.conf.urls import handler500
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.storage import staticfiles_storage



from .sitemaps import PortalSitemap
from .errors.views import page_not_found_view_404
from .errors.views import page_internal_server_error_500

# Main urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    # path('discus/', include('discus.urls')),
    path('customer/', include('customer.urls')),
    path('accounts/', include('allauth.urls')),
    # path("debug/", include("debug_toolbar.urls")),
    path('', include('main_page.urls')),
]

# Erros pages
handler404 = page_not_found_view_404
handler500 = page_internal_server_error_500

# Debuging
if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
    urlpatterns += (path("debug/", include("debug_toolbar.urls")),)
    
    
# For SEO
# https://django.fun/ru/docs/django/4.2/ref/contrib/sitemaps/
sitemaps = {
    'exhibist': PortalSitemap
}

urlpatterns += [
    # https://django.fun/ru/articles/tutorials/kak-dobavit-robotstxt-na-svoj-sajt-django/
    re_path(r'^robots\.txt$',
        TemplateView.as_view(template_name = 'robots.txt',
                             content_type='text/plain')),
    
    # https://docs.djangoproject.com/en/4.2/ref/contrib/sitemaps/
    re_path(r'^sitemap\.xml$',
            sitemap, {'sitemaps': sitemaps},
            name='django.contrib.sitemaps.views.sitemap'),
    # https://simpleit.rocks/python/django/django-favicon-adding/
    re_path(
        r"^favicon\.ico$",
        RedirectView.as_view(
            url=staticfiles_storage.url("favicon.ico")),
        name='favicon',
    ),
]