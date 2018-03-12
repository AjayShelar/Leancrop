from django.contrib import admin

# Register your models here.

from .models import Farmerdata, Farmdata, Scheduledata

admin.site.register(Farmerdata)
admin.site.register(Farmdata)
admin.site.register(Scheduledata)