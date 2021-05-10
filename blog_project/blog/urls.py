from django.contrib import admin
from django.urls import path
from blog import views
from .views import *

urlpatterns = [
    path('home/', PostListView.as_view(), name="home"),
    path('new/', PostCreateView.as_view(), name="new"),
    path('detail/<int:pk>/',PostDetailView.as_view(),name='detail'),
    path('update/<int:pk>/',PostUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',PostDeleteView.as_view(),name='delete'),
    path('about/',views.about,name="about"),
]
