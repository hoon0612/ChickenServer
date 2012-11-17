# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Stores.models import *
import json

from django.forms import ModelForm
from django.core import serializers

class StoreForm(ModelForm):
    class Meta:
        model = Store

class CategoryForm(ModelForm):
    class Meta:
        model = Category

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ('store',)

def store_list(request):
    store_list = Store.objects.all()
    
    return render(request, "store_list.djhtml", {"store_list": store_list})

def store_list_json(request):
    store_list = Store.objects.all()
    data       = serializers.serialize("json", store_list)    

    return HttpResponse(data)

def store_view(request, store_id):

    store = Store.objects.get(pk=store_id)
    review_list = Review.objects.filter(store=store)
    form = ReviewForm(initial = {"store": store_id })

    for ct in store.category.all():
        print ct.name
    
    return render(request, "store_view.djhtml",
                  {"store": store,
                   "review_list": review_list,
                   "store_id": store_id,
                   "comment_form": form})


def store_register(request):

    if request.method == "POST":
        form = StoreForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/")
    else:
        form = StoreForm()

    keys = form.fields.keys()

    for key in keys:
        form.fields[key].widget.attrs = {'class':'span6'}
    
    return render(request, "store_register.djhtml",
                  {"form": form})

def review_register(request, store_id):

    if request.method == "POST":
        form = ReviewForm(request.POST)
        form.store = Store.objects.get(pk=int(store_id))
        
        if form.is_valid():
            form.save()
    else:
        form = ReviewForm()
    
    return HttpResponseRedirect("/store_view/%s/" %(store_id,))

def category_register(request):

    category_list = Category.objects.all()

    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            
    else:
        form = CategoryForm()
        
    return render(request, "category_register.djhtml",
                  {"category_list": category_list,
                   "form": form})
