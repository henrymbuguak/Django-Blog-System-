from django.shortcuts import render_to_response

from firstblog.models import posts

def home(request):
    blogPosts = posts.objects.all()[:10]
    return render_to_response('index.html',{'blogPosts': blogPosts})

