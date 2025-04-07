from django.shortcuts import render,redirect
from django.http import Http404
from accounts.decorators import (
    login_required
)
from .models import (
    Post,Contact
)
# Create your views here.

def post_list(request):
    if request.method == 'POST':
        posts = Post.objects.filter(status = 'Published').order_by('-published_date')
    else:
        posts = Post.objects.filter(status = 'Published').order_by('-published_date')[:5]
    return render(request,'index.html',{'posts':posts})

@login_required
def post_detail(request,slug):
    try:
        post = Post.objects.get(slug = slug)
        return render(request,'post.html',{'post':post})
    except Post.DoesNotExist:
        return Http404("Post Not Found.")
    
@login_required
def contact(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        email = data.get('email')
        message = data.get('message')
        Contact.objects.create(
            username = username,
            email = email,
            description = message
        )
        return redirect('home')
    return render(request,'contact.html')

@login_required
def about(request):
    return render(request,'about.html')