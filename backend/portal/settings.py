# -*- coding: utf-8 -*-
import os

DEBUG = int(os.environ.get("DEBUG", default=False))
if DEBUG:
    from .app_settings.dev_settings import *
else:
    from .app_settings.prod_settings import *