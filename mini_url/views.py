# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from models import myURL


def list(request):
    """Display list of redirection"""
    urls = myURL.objects.order_by('-accessNb')
    return render(request, 'mini_url/list.html')



