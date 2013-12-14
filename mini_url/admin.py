from django.contrib import admin
from models import myURL


class myURLAdmin(admin.ModelAdmin):
    list_display = ('url', 'username', 'date', 'secret', 'accessNb', 'date')
    list_filter = ('username', )
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('url',)


admin.site.register(myURL, myURLAdmin)