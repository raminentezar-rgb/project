from django.urls import path
from . import views


urlpatterns = [
    path('',views.agent,name='agency')
]