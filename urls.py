
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path("",views.index ,name="index"),
    path("blog/old__url",views.old_url,name="old_url_page"),
    
    path("post/detail/<str:post_id>",views.detail,name="post_details"),
    
    path("contact",views.contact_view,name='contact'),
    
    path("new__url",views.new_url,name = "new_page_url"),
    
    path("about",views.about_view,name="about")
    
    
]
