from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course

# Create your views here.


class CourseListView(ListView):
    model = Course
    template_name = "content/course_list.html"
    # queryset = Course.objects.all()


class CourseDetail(DetailView):
    model = Course
    template_name = "content/course_detail.html"
