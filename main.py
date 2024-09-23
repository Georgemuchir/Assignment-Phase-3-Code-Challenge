# main.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_student_info(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}"

class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_students(self):
        return [student.name for student in self.students]

    def average_student_age(self):
        total_age = sum(student.age for student in self.students)
        return total_age / len(self.students) if self.students else 0

# Running the code
if __name__ == "__main__":
    course = Course("Math", "MTH101")
    student1 = Student("Alice", 21, "S001")
    student2 = Student("Bob", 22, "S002")

    course.add_student(student1)
    course.add_student(student2)

    print(course.get_students())  # Expect ['Alice', 'Bob']
    print(course.average_student_age())  # Expect 21.5
