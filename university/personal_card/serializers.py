from rest_framework import serializers
from .models import PersonalCardStudent, Student, Course, Teacher, SemesterCourse, Semester


class PersonalCardStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalCardStudent
        fields = ['id', 'name']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'number_course']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'rank']


class SemesterSerializer(serializers.ModelSerializer):
    teacher_id = serializers.SlugRelatedField(slug_field='last_name', queryset=Teacher.objects.all())

    class Meta:
        model = Semester
        fields = ['teacher_id', 'number_semester']


class SemesterCourseSerializer(serializers.ModelSerializer):
    id_course = serializers.SlugRelatedField(slug_field='number_course', queryset=Course.objects.all())
    id_semester = SemesterSerializer()

    class Meta:
        model = SemesterCourse
        fields = ['id_course', 'id_semester', 'date_begin', 'completion_date']










