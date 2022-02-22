from django.shortcuts import render

from django.views import generic
from blog.models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(published="True").order_by('-date_modified')
    template_name = 'index1.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail1.html'

