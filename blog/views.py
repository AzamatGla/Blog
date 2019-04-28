from django.views import generic
from .models import Post
from django.urls import reverse_lazy

class HomepageView(generic.ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'


class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'details'


class BlogCreateView(generic.CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'author', 'text']


class BlogUpdateView(generic.UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = ['title', 'text']


class BlogDeleteView(generic.DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')