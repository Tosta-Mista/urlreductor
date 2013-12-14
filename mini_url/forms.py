# -*- coding: utf-8 -*-
from django import forms
from models import myURL


class myURLForm(forms.Form):
    class Meta:
        model = myURL
        fields = ('url', 'username')