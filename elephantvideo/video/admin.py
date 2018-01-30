from django.contrib import admin
from .models import Company, Channel, Clip, Log
# Register your models here.

admin.site.register(Company)
admin.site.register(Channel)
admin.site.register(Clip)
admin.site.register(Log)