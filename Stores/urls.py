from django.conf.urls import patterns, include, url
import Stores.views

urlpatterns = patterns('',
    # Examples:
    # Uncomment the next line to enable the admin:
    url(r'^store_list/$', 'Stores.views.store_list'),
    url(r'^store_list_json/$', 'Stores.views.store_list_json'),
    url(r'^store_view/(?P<store_id>\d+)/$', 'Stores.views.store_view'),
    url(r'^store_register/$', 'Stores.views.store_register'),
    url(r'^category_register/$', 'Stores.views.category_register'),
    url(r'^review_register/(?P<store_id>\d+)/$', 'Stores.views.review_register'),
)
