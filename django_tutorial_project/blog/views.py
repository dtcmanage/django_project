from django import http
from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'DannyTCM',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'Feb 6, 2021',
    },
    {
        'author': 'Jan Doe',
        'title': 'Blog Post 2',
        'content': 'second Post content',
        'date_posted': 'Feb 6, 2021',
    }
    

]

def home(request):
    context={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About' })