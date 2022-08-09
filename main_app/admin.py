from django.contrib import admin

from .models import Canine, Grooming

# Register your models here.
admin.site.register(Canine)
admin.site.register(Grooming)