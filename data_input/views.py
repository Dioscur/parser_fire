# -*- coding: utf-8 -*-
import os, os.path
from django.shortcuts import render_to_response
from data_input.forms import DataForm
from django.http import HttpResponseRedirect
from urllib.request import urlretrieve, pathname2url
from urllib.parse import urljoin
from lxml.html import parse, fromstring
import requests
import  xlwt, xlrd
from mysite.settings import MEDIA_ROOT

def parser(request):
    data = []
    if request.method == "POST":
        form = DataForm(request.POST)

        if form.is_valid():
            # parser

            URL = form.cleaned_data['url']
            PATH = form.cleaned_data['tags']
            response = requests.get(URL)
            page = fromstring(response.text)
            if page.xpath(PATH):
                data = (page.xpath(PATH))
            xls_name = 'Test.xls'
            wb = xlwt.Workbook()
            ws = wb.add_sheet('Test', cell_overwrite_ok=True)
            i = 0
            for d in data:
                ws.write(i, 0, d)
                i = i + 1
            os.chdir(os.path.join(MEDIA_ROOT))
            wb.save(xls_name)
            return render_to_response("complet.html", {'data': data, 'form': form, 'xls_name': xls_name})

    else:
        form = DataForm(initial = {'url': 'http://', 'tags': '//'})

    return  render_to_response("index.html", {'form': form})


# def complet(request):
# 	return render_to_response("data_input/complet.html")