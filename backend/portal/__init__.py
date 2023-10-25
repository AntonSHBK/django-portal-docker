# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.utils.translation import gettext_lazy as _

from .celery import app as celery_app

__all__ = ("celery_app")

_("Slug")