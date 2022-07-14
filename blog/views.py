from blog.models import Post
# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# posts = [
#     {
#     'Author': 'Amitabh',
#     'Title': 'Blog Post 1',
#     'Content' : 'Photography is nowadays very handy...',
#     'Date_posted'   : 'October 28, 2007'
#     },
#     {
#     'Author': 'Andrew',
#     'Title': 'Blog Post 2',
#     'Content' : 'Political parties are becoming very wealthy...',
#     'Date_posted'   : 'April 9,2016'
#     },
#     {
#     'Author': 'James',
#     'Title': 'Blog Post 3',
#     'Content' : 'Python is a versatile language...',
#     'Date_posted'   : 'September 16,2018'
#     }
#     ]

# def  index(request):
#     return HttpResponse('<h1> Welcome to my blog</h1>')

def home(request):
    context = {'p': Post.objects.all()}      
    return render(request, 'blog/home.html',context)
# create a context then pass


def about(request):     
    return render(request, 'blog/about.html',{'title': 'About'})
# directly write the context

