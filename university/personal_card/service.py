from django_filters import rest_framework as filters
from .models import Teacher, Student, Semester


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class StudentFilter(filters.FilterSet):
    last_name = CharFilterInFilter(field_name='last_name')

    class Meta:
        model = Student
        fields = ['last_name']


class TeacherFilter(filters.FilterSet):
    class Meta:
        model = Teacher
        fields = ['rank', 'last_name', 'first_name']
