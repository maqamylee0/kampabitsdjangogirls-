from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone



# Create your views here.
def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")    

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})