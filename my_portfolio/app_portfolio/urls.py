from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns=[
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('education/',views.education, name="education" ),
    path('skills/',views.skills, name="skills" ),
    path('projects/',views.projects, name="projects" ),
    path('contact/',views.contact, name="contact" ),
    path('blog/',views.blog, name="blog" ),

]
