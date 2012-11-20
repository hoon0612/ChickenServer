from django.conf.urls import patterns, include, url
import Stores.views

urlpatterns = patterns('',
    # Examples:
    # Uncomment the next line to enable the admin:
    url(r'^store_list/$', 'Stores.views.store_list'),
    url(r'^store_list_json/$', 'Stores.views.store_list_json'),
    url(r'^store_list_jsonp/$', 'Stores.views.store_list_jsonp'),
    url(r'^store_detail_jsonp/$', 'Stores.views.store_detail_jsonp'),
    url(r'^store_view/(?P<store_id>\d+)/$', 'Stores.views.store_view'),
    url(r'^store_register/$', 'Stores.views.store_register'),
    url(r'^category/$', 'Stores.views.category'),
    url(r'^geocode/$', 'Stores.views.geocode'),
    url(r'^review_register/(?P<store_id>\d+)/$', 'Stores.views.review_register'),
)
