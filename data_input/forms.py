# -*- coding: utf-8 -*-
__author__ = 'linvv'

from django import forms

class DataForm(forms.Form):
    url = forms.CharField(max_length = 200, label = "Адрес:")
    tags = forms.CharField(max_length = 200, label = "XPath:")