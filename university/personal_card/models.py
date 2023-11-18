from django.db import models


class PersonalCardStudent(models.Model):
    name = models.CharField(max_length=15, verbose_name='name')

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.OneToOneField('PersonalCardStudent', on_delete=models.CASCADE)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.last_name


class Course(models.Model):
    student_id = models.ManyToManyField('Student', verbose_name='student')
    name = models.CharField(max_length=20)
    number_course = models.IntegerField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=15, verbose_name='First name')
    last_name = models.CharField(max_length=10, verbose_name='Last name')
    rank = models.CharField(max_length=10, verbose_name='Rank')

    def __str__(self):
        return self.last_name


class SemesterCourse(models.Model):
    id_course = models.ForeignKey('Course', on_delete=models.CASCADE)
    id_semester = models.ForeignKey('Semester', on_delete=models.CASCADE)
    date_begin = models.DateTimeField()
    completion_date = models.DateTimeField()


class Semester(models.Model):
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    number_semester = models.IntegerField()

    def __str__(self):
        return self.number_semester





