from django.contrib import admin

# Register your models here.
from .models import booking, menu
# Register yor models here.
admin.site.register(menu)
admin.site.register(booking)
