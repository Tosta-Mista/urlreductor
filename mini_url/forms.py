# -*- coding: utf-8 -*-
from django import forms
from models import myURL


class myURLForm(forms.ModelForm):
    class Meta:
        model = myURL
        fields = ('url', 'username')