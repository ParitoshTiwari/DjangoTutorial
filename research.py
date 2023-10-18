# Class example


class Student:
    # default constructor
    def __init__(self) -> None:
        self.name = "Initial Name"
        self.age = 2
        self.student_id = 10000
        self.gpa = 1.0
    

    # paramterised constructor
    def __init__(self, name, age, student_id, gpa):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.gpa = gpa

    def calculateGraduationYear(self, current_year, course_year):
        return current_year + course_year
    
    def printStudentData(self):
        print("Student Name: ", self.name)
        print("Student Age: ", self.age)
        print("Student Id: ", self.student_id)
        print("Student GPa: ", self.gpa)


if __name__ == '__main__':
    student1 = Student('Paritosh', 29, 10002, 3.9)
    student1.calculateGraduationYear(2023, 1)
    student1.printStudentData()