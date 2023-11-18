from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import *
from .models import Student, Course, SemesterCourse, Teacher
from .serializers import PersonalCardStudentSerializer, StudentSerializer, CourseSerializer, \
    SemesterCourseSerializer, TeacherSerializer
from .service import StudentFilter, TeacherFilter


class CreatePersonalCardAPIView(generics.CreateAPIView):
    """ Создание личной карты студента
    return: id студента, имя
    """
    serializer_class = PersonalCardStudentSerializer

    def create_card(self, request, *args, **kwargs):
        serializer = PersonalCardStudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateStudentAPIView(generics.CreateAPIView):
    """ Создание профиля студента
    return: id, имя, фамилия
    """

    serializer_class = StudentSerializer

    def create_student(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentAPIView(generics.ListAPIView):
    """Просмотр всех студентов в базе данных"""

    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        return queryset


class SearchStudent(generics.ListAPIView):
    """Поиск в базе данных через URL студентов по фамилии"""

    filter_backends = (DjangoFilterBackend,)
    serializer_class = StudentSerializer
    filters_class = StudentFilter

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        queryset = Student.objects.filter(last_name__icontains=name)
        return queryset


class CreateCourse(generics.CreateAPIView):
    """Создание курса
    param: Название курса, номер курса.
    """
    serializer_class = CourseSerializer

    def create_course(self, request, *args, **kwargs):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CourseAPIView(generics.ListAPIView):

    """Просмотреть все записи таблицы курс"""

    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        return queryset


class SemesterCourseAPIView(generics.ListAPIView):

    """Просмотреть записи в таблице семестр - курс """

    serializer_class = SemesterCourseSerializer

    def get_queryset(self):
        queryset = SemesterCourse.objects.all()
        return queryset


class TeacherAPIView(generics.ListAPIView):

    """Просмотр всех записей в таблице учитель"""

    serializer_class = TeacherSerializer

    def get_queryset(self):
        queryset = Teacher.objects.all()
        return queryset


class CreateTeacherAPIView(generics.CreateAPIView):

    """Создание записи учитель"""

    serializer_class = TeacherSerializer

    def create_teacher(self, request, *args, **kwargs):
        serializer = TeacherSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateDestroyTeacher(generics.RetrieveUpdateDestroyAPIView):

    """Обновление и удаление записей в таблице учитель"""

    serializer_class = TeacherSerializer

    def destroy_teacher(self, request, pk=None, *args, **kwargs):
        instance = get_object_or_404(Teacher, pk=pk)
        instance.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    def update_teacher(self, pk=None, *args, **kwargs):
        instance = get_object_or_404(Teacher, pk)
        instance.update()
        return Response(status=HTTP_204_NO_CONTENT)

    def get_queryset(self):
        queryset = Teacher.objects.all()
        return queryset


class SearchTeacher(generics.ListAPIView):

    """Поиск учителя по фамилии или по званию"""

    filter_backends = (DjangoFilterBackend,)
    serializer_class = TeacherSerializer
    filters_class = TeacherFilter

    def get_queryset(self):

        query_name = self.request.query_params.get('name', '')
        if query_name:
            queryset = Teacher.objects.filter(last_name__icontains=query_name)

        query_name = self.request.query_params.get('rank', '')
        if query_name:
            queryset = Teacher.objects.filter(rank__icontains=query_name)

        return queryset
