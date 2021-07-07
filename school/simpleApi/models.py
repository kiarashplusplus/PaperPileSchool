from django.db import models
from django.contrib.auth.models import User


class Teacher(User):
    class Meta:
        verbose_name_plural = "Teachers"

class Student(User):
    class Meta:
        verbose_name_plural = "Students"

class Gradeable(models.Model):
    id = models.AutoField(name="gradeable_id", primary_key=True)
    name = models.CharField(max_length=100)
    student = models.IntegerField()
    submission_datetime = models.DateTimeField(auto_now_add=True)
    grading_datetime = models.DateTimeField(null=True, blank=True)
    document = models.FileField(upload_to='uploads/%Y/%m/%d/')
    grade = models.TextField(default="ungraded")
    teacher_notes = models.TextField(blank=True)
