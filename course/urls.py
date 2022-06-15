from django.urls import path
from .views import CourseListView, CourseDetail

urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('<slug>/', CourseDetail.as_view(), name='course-detail')
]
