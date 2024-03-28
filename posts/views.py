from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.views.generic import ListView , DetailView
# Create your views here.

def create_post(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST,request._files)
        if form.is_valid():
            form.save()
    else:    
        form = PostForm()

    return render(request , 'posts/new.html' , {'form':form})

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post
    


'''
def post_detail(request,post_id):
    data = Post.objects.get(id=post_id)
    context = {
        'post' : data
    }
    return render (request , 'posts/post_detail.html',context)
'''
'''
def post_list(request):
    data = Post.objects.all() 
    context = {
        'mahmoud' : data
    }
    return render(request,'posts/post_list.html',context)
'''