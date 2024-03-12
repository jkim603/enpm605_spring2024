class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []  # List to hold courses the student enrolls in

    def enroll(self, course):
        self.courses.append(course)
        course.students.append(self)  # Add this student to the course's student list


class Course:
    def __init__(self, title):
        self.title = title
        self.students = []  # List to hold students enrolled in the course

    def add_student(self, student):
        self.students.append(student)
        student.courses.append(self)  # Add this course to the student's course list


# Creating instances of each class
student1 = Student("Alice")
course1 = Course("Introduction to Python")

# Enrolling the student in the course (and vice versa)
student1.enroll(course1)

# Alternatively, adding the student to the course (which also enrolls them in the course)
# course1.add_student(student1)

# Demonstrating the bidirectional relationship
print(
    f"Students enrolled in {course1.title}: {[student.name for student in course1.students]}"
)
print(
    f"Courses {student1.name} is enrolled in: {[course.title for course in student1.courses]}"
)
