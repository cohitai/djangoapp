from django.shortcuts import render
from django.http import HttpResponseRedirect

from blog.models import Post

# Create your views here.


def index(request):
    return render(request, 'mainview/index.html')


def products(request):
    return render(request, 'mainview/product.html')


def contact(request):
    return render(request, 'mainview/contact.html')


#def blog(request):
    #return render(request, 'mainview/blog.html')


def redirect(request, **kwargs):
    return HttpResponseRedirect('http://localhost:%s' % kwargs.get('var'))


def blog(req):
    all_posts = Post.objects.all()
    return render(req, 'mainview/blog.html', {'posts': all_posts})
