from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Post,AboutUs
import logging
from django.core.paginator import Paginator
from django.http import Http404

from.forms import ContactForm


#posts=[
#        { "id":"1","title":"post","content":"content of post 1 "},
 #       { "id":"2","title":"post","content":"content of post 2"},
  #      { "id":"3","title":"post","content":"content of post 3"},
   #     { "id":"4","title":"post","content":"content of post 4"}
    #]
    # Create your views here.


def index(request):
    
    blog_title = "hello posts"
    
    all_posts=Post.objects.all()
    
    paginator = Paginator(all_posts,5)
    
    page_number=request.GET.get('page')
    
    page_obj=paginator.get_page(page_number)
    
   
    return render(request,"index.html",{"page_obj":page_obj})


def detail(request,post_id):
    
    
    
    
    #post = next((item for item in posts if item["id"] == post_id),None)
    try:
        post=Post.objects.get(pk=post_id)
        
        related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)
        
    except Post.DoesNotExist:
        
        raise Http404("post doesn not exits")
    
    return render(request,"detail.html",{"post":post,'related_posts':related_posts})



    
    

def old_url(request):
    
    return redirect(reverse('blog:new_page_url'))

def new_url(request):
    
    return HttpResponse("this is new page url")


def contact_view(request):
    
    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        
        
    
    return render(request,"contact.html")
def about_view(request):
    
    about_content=AboutUs.objects.first().content
    
    
    
    return render(request,"about.html",{'about_content':about_content})
    
    


    
    
    
    
