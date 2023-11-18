"""
URL configuration for university project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from personal_card.views import CreatePersonalCardAPIView, CreateStudentAPIView, StudentAPIView, CreateCourse,\
    CourseAPIView, SemesterCourseAPIView,TeacherAPIView,CreateTeacherAPIView, UpdateDestroyTeacher, SearchStudent,\
    SearchTeacher

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/personal_card/', CreatePersonalCardAPIView.as_view()),
    path('api/v1/student/', CreateStudentAPIView.as_view()),
    path('api/v1/student/all/', StudentAPIView.as_view()),
    path('api/v1/student/search/', SearchStudent.as_view()),
    path('api/v1/course/', CreateCourse.as_view()),
    path('api/v1/course/all/', CourseAPIView.as_view()),
    path('api/v1/sem_cours/all/', SemesterCourseAPIView.as_view()),
    path('api/v1/teacher/all/', TeacherAPIView.as_view()),
    path('api/v1/teacher/', CreateTeacherAPIView.as_view()),
    path('api/v1/teacher/<int:pk>', UpdateDestroyTeacher.as_view()),
    path('api/v1/teacher/search/', SearchTeacher.as_view()),
]

