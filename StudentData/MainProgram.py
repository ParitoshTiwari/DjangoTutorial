from functools import reduce

import win32com.client
from Students import Student

if __name__ == '__main__':
    # s = Student(teacher_code = 12, teacher_name = 'Mr X', teacher_classes = ['OOPS', 'Basic Python'], teacher_clubs = ['Some club', 'new club'], subject_code = 'ab001', number_of_classes = 16, number_of_exams = 1, subject_professor = 'Mr. X')
    # s.teacher_name = 'check prof'
    # s.number_of_exams = 6
    # s.number_of_classes = 9

    # s.printAllData()

    # lst = [1,5,9,10,12,14,15]
    # lst2 = [2,6,10,11,13,15,16]
    
    # filter is used to filter iterable with some number
    # kgh = list(filter(lambda c: c > 10, lst)) #thats one way to do

    # map is used to iterate on iterables and then applying operation
    # kgh = list(map(lambda c : c * c, lst))

    # reduces a number with some operation or logic
    # kgh = reduce(lambda c, d: c * d, lst)

    # kgh = [num for num in lst if num > 10]
    # print(kgh)

    # some = [(x, y) for x in lst for y in lst2]
    # print(some)
    # excel = win32com.client.Dispatch("Excel.Application")

    # Make the application visible
    # excel.Visible = True

    # Create a new workbook
    # workbook = excel.Workbooks.Add()

    # Access the first worksheet
    # worksheet = workbook.Worksheets(1)

    # Set the value of cell A1 to "Hello World"
    # worksheet.Cells(1, 1).Value = "Hello World"

    # print(dir(tuple))
    # Initialize to -1
    # dp = []

    # # This function returns the number of
    # # arrangements to form 'n'
    # def solve(n):
    #     # base case
    #     if n < 0:
    #         return 0
    #     if n == 0:
    #         return 1

    #     if dp[n] != -1:
    #         return dp[n]

    #     dp[n] = solve(n-1) + solve(n-3) + solve(n-5)
    #     return dp[n]

    # print(solve(5))
    # def binary_search(list, item, low, high):
    #     if low <= high:
    #         mid = (low + high) // 2
    #         guess = list[mid]
    #         if guess == item:
    #             return mid
    #         elif guess > item:
    #             return binary_search(list, item, low, mid - 1)
    #         else:
    #             return binary_search(list, item, mid+1, high)
    #     else:
    #         return None
        
    # my_list = [1, 3, 5, 7, 9]
    # low = 0
    # high = len(my_list) - 1
    # print(binary_search(my_list, 3, low, high)) # => 1
    # print(binary_search(my_list, 9, low, high))

    def firstMissingPositive(nums) -> int:
        a = sorted(nums)
        b = a[0]
        for i in a:
            if b < 0:
                b += 1
                continue
            elif b == 0:
                b += 1
                continue
            elif i != b:
                b += 1
                return b
            else:
                return b
        return b
    
    print(firstMissingPositive([3,4,-1,1]))