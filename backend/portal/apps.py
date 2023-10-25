# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import logging

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NashRegionConfig(AppConfig):
    name = 'portal'
    verbose_name = _("My portal")
    logger = logging.getLogger('logfile')
