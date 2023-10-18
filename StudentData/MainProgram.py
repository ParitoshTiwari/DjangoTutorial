from Students import Student

if __name__ == '__main__':
    s = Student(teacher_code = 12, teacher_name = 'Mr X', teacher_classes = ['OOPS', 'Basic Python'], teacher_clubs = ['Some club', 'new club'], subject_code = 'ab001', number_of_classes = 16, number_of_exams = 1, subject_professor = 'Mr. X')
    # s.teacher_name = 'check prof'
    # s.number_of_exams = 6
    # s.number_of_classes = 9

    s.printAllData()