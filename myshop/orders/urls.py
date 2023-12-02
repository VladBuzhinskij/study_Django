
from django.urls import include, re_path
from . import views
app_name='orders'

urlpatterns = [
    re_path(r'^create/$', views.order_create, name='order_create'),
]