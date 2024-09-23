# tests.py
import unittest
from main import Person, Student, Course

class TestPerson(unittest.TestCase):
    def test_person_introduce(self):
        person = Person("John", 30)
        self.assertEqual(person.introduce(), "Hi, my name is John and I am 30 years old.")

class TestStudent(unittest.TestCase):
    def test_student_info(self):
        student = Student("Alice", 21, "S001")
        self.assertEqual(student.get_student_info(), "Student ID: S001, Name: Alice, Age: 21")

class TestCourse(unittest.TestCase):
    def test_add_student(self):
        course = Course("Math", "MTH101")
        student = Student("Alice", 21, "S001")
        course.add_student(student)
        self.assertEqual(course.get_students(), ["Alice"])

    def test_average_student_age(self):
        course = Course("Math", "MTH101")
        student1 = Student("Alice", 21, "S001")
        student2 = Student("Bob", 22, "S002")
        course.add_student(student1)
        course.add_student(student2)
        self.assertEqual(course.average_student_age(), 21.5)

if __name__ == "__main__":
    unittest.main()
