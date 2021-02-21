from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

# Create your views here.

class BlogListViews(ListView):
    model = Post
    template_name = 'blog/inc/home.html'
    context_object_name = 'posts'

class BlogDetailPost(DetailView):
    model = Post
    template_name = 'blog/inc/post_detail.html'
    context_object_name = 'post'

class BlogAddPost(CreateView):
    model = Post
    template_name = 'blog/inc/add_post.html'
    fields = ['title','author','body']
    #context_object_name = 'post'


