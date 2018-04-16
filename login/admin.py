# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from feiyu.admin import admin_site
from . import models
admin_site.register(models.User)