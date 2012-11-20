# -*- coding: utf-8 -*-

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
#        exclude = ('store',)

def store_list(request):
    store_list = Store.objects.all()
    
    return render(request, "store_list.djhtml", {"store_list": store_list})

def store_list_json(request):
    store_list = Store.objects.all()
    data       = serializers.serialize("json", store_list,
                                       fields=('pk','locationX', 'locationY', 'name'))    

    return HttpResponse(data)

def store_list_jsonp(request):

    if request.method == "GET" and request.GET.has_key(u'callback'):

        callback = request.GET[u'callback']
        
        store_list = Store.objects.all()

        if request.GET.has_key(u'category'):
            category = request.GET['category']

            #store_list = store_list.filter(category__in=

        if request.GET.has_key(u'x') and request.GET.has_key(u'y'):
            (x, y) = (request.GET[u'x'],request.GET[u'y'])

            store_list2 = []
            
            for store in store_list:
                (x2,y2)=(store.locationX,store.locationY)
                dist = ((x-x2)**2 + (y-y2)**2) ** 0.5
                store_list2 += [(dist, store)]

            store_list2.sort()
            store_list = store_list2
        
        data = serializers.serialize("json", store_list[:min(5, len(store_list))] )

        jsonp = callback + "(" +  data + ");"
        
        return HttpResponse(jsonp)
    else:
        return HttpResponse('-1')

def store_detail_jsonp(request):
    if request.method == "GET" and request.GET.has_key(u'pk') and request.GET.has_key(u'callback'):
        callback = request.GET[u'callback']
        store_list = Store.objects.filter(pk=int(request.GET[u'pk']))
        data = serializers.serialize("json", store_list)
        
        jsonp = callback + "(" +  data + ");"
        
        return HttpResponse(jsonp)
    else:
        return HttpResponse('-1')


def store_view(request, store_id):

    store = Store.objects.get(pk=store_id)
    review_list = Review.objects.filter(store=store)

    form = ReviewForm(initial = {"store": int(store_id) })

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

        form = ReviewForm(request.POST, request.FILES,
                          initial = {"store": int(store_id) })
#        form.store = Store.objects.get(pk=int(store_id))
        form.store = int(store_id)
        
        if form.is_valid():
            form.save()
    
    return HttpResponseRedirect("/store_view/%s/" %(store_id,))

def category(request):

    category_list = Category.objects.all()

    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            
    else:
        form = CategoryForm()
        
    return render(request, "category_register.djhtml",
                  {"category_list": category_list,
                   "form": form})

def geocode(request):

    if request.method == "GET" and request.GET.has_key(u'addr'):

        import urllib, re

        url = 'http://openapi.map.naver.com/api/geocode.php?key=f4d26c0529617faf266e90673fca3d8d&coord=LatLng&query=' + request.GET[u'addr'].encode('utf-8')
    
        ret = urllib.urlopen(url).read()

        iterator = re.finditer(r"<x>([\d\.]+)</x>",ret, re.DOTALL)
        x = [k.group(1) for k in iterator]

        if len(x) < 1:
            return HttpResponse("-2")
        iterator = re.finditer(r"<y>([\d\.]+)</y>",ret, re.DOTALL)
        y = [k.group(1) for k in iterator]

        return HttpResponse(x[0] + "/" + y[0])
    else:
        return HttpResponse("-1")
    
