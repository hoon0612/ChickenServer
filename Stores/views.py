# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from Stores.models import *
import json

def store_list(request):
    store_list = Store.objects.all()
    
    return render(request, "store_list.djhtml", {"store_list": store_list})

def store_view(request, store_id):

    print store_id

    store = Store.objects.get(pk=store_id)
    review_list = Review.objects.filter(store=store)
    
    return render(request, "store_view.djhtml", {"store": store,
                                                 "review_list": review_list})

def store_register(request):
    return render(request, "store_register.djhtml")
