from django.db import models


class myURL(models.Model):
    url = models.URLField(verbose_name='Your base url', unique=True)
    secret = models.CharField(verbose_name='My Secret Key', max_length=10, unique=True)
    username = models.CharField(verbose_name='Nickname', max_length=255, blank=True, null=True)
    accessNb = models.IntegerField(default=0, verbose_name='Number of access allowed')
    date = models.DateTimeField(verbose_name='Added', auto_now_add=True)

    class Meta:
        verbose_name="URL Reductor"