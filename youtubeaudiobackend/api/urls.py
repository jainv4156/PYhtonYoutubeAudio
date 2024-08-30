
from django.urls import path,include
from . import views

urlpatterns = [
    path('audio', views.audio, name='audio'),
    path('demo', views.demoRequest, name='demo'),

]
