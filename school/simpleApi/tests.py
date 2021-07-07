from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from simpleApi.models import Teacher, Student, Gradeable

class TeacherTestCase(TestCase):
    def setUp(self):
        Teacher.objects.create(username="teacher1", password="teacher", first_name="teacher")
        Student.objects.create(username="student1", password="student", first_name="student")

    def test_teacher_is_setup(self):
        teacher = Teacher.objects.get(username="teacher1")
        self.assertEqual(teacher.get_full_name(), "teacher")

    def test_student_is_setup(self):
        student = Student.objects.get(username="student1")
        self.assertEqual(student.get_full_name(), "student")
    
    def test_create_gradeable(self):
        
        g = Gradeable(name="homework1")
        g.student = Student.objects.get(username="student1")
        g.document = SimpleUploadedFile(
            "best_file_eva.txt",
            b"these are the file contents!"
        )
        g.save()
        self.assertEqual(g.grade, "ungraded")
