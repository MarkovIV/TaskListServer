from django.contrib import admin
from .models import Helper

# Register your models here.

class HelperAdmin(admin.ModelAdmin):
    list_display  = ('id', 'task', 'date', 'done', 'priority', 'delete')
    list_display_links = ('id', 'task')
    search_fields = ('id', 'task')
    list_editable = ('done', 'delete')
    list_filter = ('done', 'date', 'priority', 'delete')

admin.site.register(Helper, HelperAdmin)
