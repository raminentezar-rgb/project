from django.urls import path
from  . import views


urlpatterns = [
    path('',views.dental,name='dentist'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('about/',views.about,name='about'),
    path('doctors/',views.doctors,name='doctors'),
    path('services/',views.services,name='services'),
    path('blog-single/',views.blog_single,name='blog_single'),
]
