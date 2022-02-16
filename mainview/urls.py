from django.urls import path, re_path
from django.shortcuts import redirect
from . import views


def get_new_url(request):
    # Specify the port number, you could get this dynamically
    # through a config file or something if you wish
    new_port = '8080'

    # `request.get_host()` gives us {hostname}:{port}
    # we split this by colon to just obtain the hostname
    hostname = request.get_host().split(':')[0]
    # Construct the new url to redirect to
    url = 'http://' + hostname + ':' + new_port + '/'
    return redirect(url)


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('products', views.products, name='products'),
    # path('blog', views.blog, name='blog'),
    path('blog', get_new_url, name='blog'),
    path('contact', views.contact, name='contact')
]


