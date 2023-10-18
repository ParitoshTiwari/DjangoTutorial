from Subjects import Subjects
from TeachingStaff import Teacher


class Student(Teacher, Subjects):
    def __init__(self, teacher_code, teacher_name, teacher_classes, teacher_clubs, subject_code, number_of_classes, number_of_exams, subject_professor):
        Teacher.__init__(self, teacher_code, teacher_name, teacher_classes, teacher_clubs)
        Subjects.__init__(self, subject_code, number_of_classes, number_of_exams, subject_professor)
    # def __init__(self, teacher_code, teacher_name, teacher_classes, teacher_clubs):
    #     super().__init__(teacher_code, teacher_name, teacher_classes, teacher_clubs)

    def printAllData(self):
        print('Teacher Name: ', self.teacher_name)
        print('Number of classes: ', self.number_of_classes)
        print('Number of exams ', self.number_of_exams)