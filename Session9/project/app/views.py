from django.shortcuts import render
from .models import Post
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts': posts})

def new(request):
    if request.method == 'POST':
        #Post.objects.create(
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail', new_post.pk)
    
    return render(request, 'new.html')

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    return render(request, 'detail.html', {'post': post})

def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post.pk).update(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail', post_pk)
    return render(request, 'update.html', {'post': post})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')