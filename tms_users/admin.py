from django.contrib import admin
from .models import TmsUsers

class TmsAdmin(admin.ModelAdmin):
    list_display = ('name','email_id','created_at')

admin.site.register(TmsUsers,TmsAdmin)
# Register your models here.
