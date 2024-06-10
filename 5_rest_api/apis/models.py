from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name

class Classroom(models.Model):
    grade = models.CharField(max_length=10)
    section = models.CharField(max_length=10)
    school = models.ForeignKey(School, related_name='classrooms', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.grade} - {self.section}'

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    classroom = models.ForeignKey(Classroom, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
