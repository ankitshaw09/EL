from django.urls import path
from .views import *

urlpatterns = [
    path("courses/categories/", CategoryListView.as_view(), name="course-categories"),
    path("courses/", CourseListView.as_view(), name="course-list"),
    path("courses/enroll/", EnrollCourseView.as_view(), name="enroll-course"),
    
    path("learning-paths/<int:userId>/", LearningPathView.as_view(), name="learning-path"),
    path("tips/", LearningTipsView.as_view(), name="learning-tips"),
]

