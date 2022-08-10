from django.contrib import admin

from .models import Canine, Grooming, Trick

# Register your models here.
admin.site.register(Canine)
admin.site.register(Grooming)
admin.site.register(Trick)