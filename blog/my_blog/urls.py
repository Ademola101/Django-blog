from django.contrib import admin
from django.urls import path,include
from .views import MultimodelView,BlogView,CategoryView,CreateCategory,CreateBlog
from . import views
urlpatterns = [
    path("",MultimodelView.as_view(), name = "home"),
    path("<slug:slug>",CategoryView.as_view(),name="category"),
    path("category/new/<slug:slug>",BlogView.as_view(),name = "post"),
    path("<slug:slug>/new",CreateCategory.as_view(),name = "new_category"),
    path("category/new/<slug:slug>/new",CreateBlog.as_view(),name = "new_post")
    ]