# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime


def index (request):
    context = {
        "date": strftime("%b %m, %Y", localtime()),
        "time": strftime("%H:%M %p", localtime()),
        "msg": "The current time and date: "
    }
    return render(request,'index.html', context)
