# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Stores.models import *
import json

from django.forms import ModelForm

def store_list(request):
    store_list = Store.objects.all()
    
    return render(request, "store_list.djhtml", {"store_list": store_list})

def store_view(request, store_id):

    print store_id

    store = Store.objects.get(pk=store_id)
    review_list = Review.objects.filter(store=store)
    
    return render(request, "store_view.djhtml",
                  {"store": store,
                   "review_list": review_list,
                   "store_id": store_id })


class StoreForm(ModelForm):
    class Meta:
        model = Store

def store_register(request):

    if request.method == "POST":
        form = StoreForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/")
    else:
        
        form = StoreForm()
    
    return render(request, "store_register.djhtml",
                  {"form": form})

def review_register(request, store_id):
    
    return HttpResponseRedirect("/store_view/%d" %(store_id,))

    
