from django.contrib import admin
from .models import Company, Channel, Clip, Log, Notification, Favorite
# Register your models here.

admin.site.register(Company)
admin.site.register(Channel)
admin.site.register(Clip)
admin.site.register(Log)
admin.site.register(Notification)
admin.site.register(Favorite)