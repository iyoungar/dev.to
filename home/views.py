from django.shortcuts import render
from django.http import HttpResponse
from home.models import UserPost
from home.models import Post

#from .form import Postform
# Create your views here.

def homepage(request):

  blog = UserPost.objects.all()
  print(blog)
  for i in blog:
    print(i.tags)
    print(i.body)
    context ={
      'blog':blog
    }



  return render (request, "main.html", context)

def posts(request):
  posts = UserPost.objects.all() 
  return render (request, "postpage.html", {'posts':posts});

 
#def postFormView(request):
  #  if request.method == 'POST':
  #      form = Postform()

  #      context = {'form':form}

   #     return render(request, 'postform.html', context) 
#-->
