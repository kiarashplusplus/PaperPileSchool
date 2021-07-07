from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from simpleApi.models import Teacher, Student, Gradeable

class TeacherTestCase(TestCase):
    def setUp(self):
        s = Student.objects.create(username="student1", password="student", first_name="student")
        Teacher.objects.create(username="teacher1", password="teacher", first_name="teacher")

        g = Gradeable(name="homework1", student=s.id)
        g.document = SimpleUploadedFile(
            "best_file_eva.txt",
            b"these are the file contents!"
        )
        g.save()

    def test_teacher_is_setup(self):
        teacher = Teacher.objects.get(username="teacher1")
        self.assertEqual(teacher.get_full_name(), "teacher")

    def test_student_is_setup(self):
        student = Student.objects.get(username="student1")
        self.assertEqual(student.get_full_name(), "student")
    
    def test_student_create_gradeable(self):
        g = Gradeable(name="homework1")
        g.student = 1
        g.document = SimpleUploadedFile(
            "best_file_eva.txt",
            b"these are the file contents!"
        )
        g.save()
        self.assertEqual(g.grade, "ungraded")
    
    def test_student_get_grades(self):
        s = Student.objects.get(username="student1")
        g = Gradeable.objects.filter(student=s.id)

        self.assertEqual(len(g), 1)

    def test_teacher_get_gradeables(self):
        g = Gradeable.objects.filter(name="homework1")
        self.assertEqual(len(g), 1)

    def test_teacher_post_grade(self):
        g = Gradeable.objects.get(name="homework1")
        g.grade = "A"
        g.notes = "Some notes !!"
        g.save()
        self.assertEqual(g.grade, "A")
