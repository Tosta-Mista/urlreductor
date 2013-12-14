from django.contrib import admin
from models import myURL


class myURLAdmin(admin.Admins):
    list_display = ('url', 'username', 'date', 'secret', 'accessNb', 'date')