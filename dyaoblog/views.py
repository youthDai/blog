from django.shortcuts import render_to_response

# Create your views here.
from dyaoblog.models import BlogPost


def myBlogs(request):
    blog_list = BlogPost.objects.all()
    return render_to_response('Blog.html', {'blog_list': blog_list})
