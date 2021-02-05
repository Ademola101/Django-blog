from django.contrib import admin
from django.urls import path,include
from .views import MultimodelView,BlogView,CategoryView
from . import views
urlpatterns = [
    path("",MultimodelView.as_view(), name = "home"),
    path("<slug:slug>",CategoryView.as_view(),name="category"),
    path("<slug:slug>/post",BlogView.as_view(),name = "post")
    ]