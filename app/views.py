from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import Post
# Create your views here.
def index(request):
    if request.method=='POST':
        if request.POST.get('title') and request.POST.get('author') and request.POST.get('blog'):
            post=Post()
            post.title=request.POST.get('title')
            post.author=request.POST.get('author')
            post.blog=request.POST.get('blog')
            post.save()
            return render(request, 'index.html')
    return render(request,'index.html')


def blog(request):
    data=Post.objects.all()
    # id=Post.objects.get(id=id)
    context={
        'data':data,
    }
    return render(request, 'blog.html', context)

def posts(request, id):
    id=Post.objects.get(id=id)
    context={
        'id':id
    }
    return render(request,'posts.html',context)