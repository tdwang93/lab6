#!/usr/bin/env python3

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Convert number to string to avoid TypeError
        self.courses = {}

    def displayStudent(self):
        return f'Student Name: {self.name}\nStudent Number: {self.number}'

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayGPA(self):
        if len(self.courses) == 0 or all(grade == 0.0 for grade in self.courses.values()):
            gpa = 0.0
        else:
            gpa = sum(self.courses.values()) / len(self.courses)
        return f'GPA of student {self.name} is {gpa:.1f}'

    def displayCourses(self):
        # Returns a list of courses with grades greater than 0.0
        passed_courses = [course for course, grade in self.courses.items() if grade > 0.0]
        return passed_courses

# Test cases can be run separately using unittest.
