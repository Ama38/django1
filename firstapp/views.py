from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(huynya):
    return HttpResponse(datetime.now())

