from django.contrib import admin

from .models import djangoClasses

# register djangoClasses so it's available on admin section of site
admin.site.register(djangoClasses)
