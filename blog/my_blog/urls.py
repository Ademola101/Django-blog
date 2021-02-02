from django.contrib import admin
from django.urls import path,include
from .views import CategoryList
urlpatterns = [
    path("",CategoryList.as_view(), name = "home")
]