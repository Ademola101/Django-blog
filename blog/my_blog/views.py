from django.shortcuts import render
from django.views.generic import ListView
from my_blog.models import BlogCategory
# Create your views here.

class CategoryList(ListView):
    model = BlogCategory
    context_object_name = "category_list"
    template_name = "my_blog/Home.html"