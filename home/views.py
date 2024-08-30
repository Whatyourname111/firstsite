from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect, HttpResponse
from django.template.context_processors import request

from .models import Blog, Area, Region
from .forms import CreateBlogForm,UpdateBlog


# Create your views here.
def home2(request):
    return render(request,"index.html")


def blogList(request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs
    }
    return render (request, 'index.html',context)


def craeteBlog(request):

    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        Blog.objects.create(

          title=title,
          body=body
        )
        return redirect('http://127.0.0.1:8000/kk/blog/')



    form = CreateBlogForm
    context = {
        "form": form

    }
    return render  (request, "blog_form.html",context)

def update_blog_view(request,id):
    blog = Blog.objects.get(pk=id)

    if request.method == "POST":
        blog = UpdateBlog(request.POST, instance=blog)
        if blog.is_valid():
            blog.save()
            return redirect("http://127.0.0.1:8000/kk/blog/")
        return HttpResponse('error')
    UpdateBlogForm = UpdateBlog(instance=blog)
    context = {

        'UpdateBlogForm':UpdateBlogForm
    }
    return render (request,"update_blog.html",context)

def deleteBlogview(request, id ):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect("http://127.0.0.1:8000/kk/blog/")

def area_show(request):
    areas = Area.objects.all()
    context = {
        'areas': areas

    }
    return render(request,"area.html",context)

def region_show(request):
    regions = Region.objects.all()
    context = {
        'regions': regions
    }
    return render(request,"region.html",context)




