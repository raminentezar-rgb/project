from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('resume/',views.resume,name='resume'),
    path('project/',views.project,name='project'),
    path('contacts/',views.contacts,name='contacts'),
]