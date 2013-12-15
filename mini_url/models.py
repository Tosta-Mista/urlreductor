# -*- coding : utf- 8 -*-
from django.db import models
import random
import string


class myURL(models.Model):
    url = models.URLField(verbose_name='Your base url', unique=True)
    secret = models.CharField(verbose_name='My Secret Key', max_length=10, unique=True)
    username = models.CharField(verbose_name='Nickname', max_length=255, blank=True, null=True)
    accessNb = models.IntegerField(default=0, verbose_name='Number of access allowed')
    date = models.DateTimeField(verbose_name='Added', auto_now_add=True)

    def __unicode__(self):
        return u'[{0}] {1}'.format(self.code, self.url)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.generate(10)

        super(myURL, self).save(*args, **kwargs)

    def generate(self, N):
        char = string.letters + string.digits
        randomize = [random.choice(char) for _ in xrange(N)]
        self.accessNb = ''.join(randomize)

    class Meta:
        verbose_name="URL Reductor"