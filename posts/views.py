from django.shortcuts import render , redirect
from .models import Post,Comment
from .forms import PostForm,CommentForm
from django.views.generic import ListView , DetailView ,CreateView ,DeleteView,UpdateView
# Create your views here.

def create_post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST,request._files)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            form.save()
            return redirect('/posts/')
    else:    
        form = PostForm()

    return render(request , 'posts/post_form.html' , {'form':form})

def edit_post(request,pk2 ):
    post = Post.objects.get(id=pk2)
    if request.method == 'POST':
        form = PostForm(request.POST,request._files,instance=post)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            form.save()
            return redirect('/posts/')
    else:    
        form = PostForm(instance=post)
    return render(request , 'posts/edit.html' , {'form':form})

def delete_post(request,pk2 ):
    post = Post.objects.get(id=pk2)
    post.delete()
    return redirect('/posts/')

def post_detail(request,pk):
    data = Post.objects.get(id=pk)
    comments=Comment.objects.filter(post=data) 
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.post = data
            myform.save()
    else:
        form = CommentForm()
    
    context = {
        'post' : data,
        'comments':comments,
        'form' : form
    }
    return render (request , 'posts/post_detail.html',context)


def post_list(request):
    data = Post.objects.all() 
    context = {
        'object_list' : data
    }
    return render(request,'posts/post_list.html',context)
