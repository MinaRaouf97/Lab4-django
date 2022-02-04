from django.contrib import admin
# Register your models here.
from .models import Intake,track


admin.site.register(track)
admin.site.register(Intake)
