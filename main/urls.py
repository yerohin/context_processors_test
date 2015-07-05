from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^local/$', 'main.views.local_item', name='main_local'),
    url(r'^$', 'main.views.global_item', name='main_global'),
]
