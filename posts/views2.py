from django.shortcuts import render , redirect
from .models import Post
from .forms import PostForm
from django.views.generic import ListView , DetailView ,CreateView ,DeleteView,UpdateView

'''
class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class AddPost(CreateView):
    model = Post
    fields = '__all__'
    success_url ='/posts/'

class EditPost(UpdateView):
    model = Post
    fields = '__all__'
    success_url ='/posts/'
    template_name = 'posts/edit.html'
class DeletePost(DeleteView):
    model = Post
    success_url ='/posts/'
    template_name = 'post_confirm_delete.html'
    '''