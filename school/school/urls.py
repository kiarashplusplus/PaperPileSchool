"""school URL Configuration

Read Endpoints.md for more details.
"""
from django.contrib import admin
from django.urls import path, include
from simpleApi.views import home, student_create_gradeable, student_get_grades, teacher_get_gradeables, teacher_post_grade

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('student/', student_get_grades, name='student_get_grades'),
    path('teacher/', teacher_get_gradeables, name='teacher_get_gradeables'),
    path('grade/', teacher_post_grade, name='teacher_post_grade'),
    path('upload/', student_create_gradeable, name='student_create_gradeable'),
]
