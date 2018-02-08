#coding=utf-8
from django.shortcuts import render

def index(request):
    res = {}
    res['msg'] = '你好，朋友。'
    return render(request, 'index.html', res)