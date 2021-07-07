from django.test import TestCase
from simpleApi.models import Teacher, Student

class TeacherTestCase(TestCase):
    def setUp(self):
        Teacher.objects.create(username="teacher1", password="teacher", first_name="teacher")

    def test_teacher_is_setup(self):
        teacher = Teacher.objects.get(username="teacher1")
        self.assertEqual(teacher.get_full_name(), "teacher")