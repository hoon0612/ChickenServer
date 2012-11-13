# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from Stores.models import *
import json

def store_list(request):

    store_list = Store.objects.all()
    
    return render(request, "store_list.djhtml", {"store_list": store_list})
