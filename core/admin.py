from django.contrib import admin
from . import models as core_models

admin.site.register(core_models.Movie)


