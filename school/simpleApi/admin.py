from django.contrib import admin
from simpleApi.models import Student, Teacher, Gradeable


admin.site.register(Gradeable)
admin.site.register(Student)
admin.site.register(Teacher)
