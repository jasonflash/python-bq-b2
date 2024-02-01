# def  a():
#     return 2+2+2+20/2*6*69
# result = a()
# print(result)


# def add_numbers(num1, num2):
#     divide = num1 / num2
#     return divide

# num1 = int(input())
# num2 = int(input())
# result = add_numbers(num1, num2)
# print(result)

###

# def add_two_numbers(*numbers):
#     size = len(numbers)
#     sum = 0
# for i in range(size):
#         sum = sum + numbers[i]
#     return sum

# num1 = 1
# num2 = 2
# num3 = 3
# result = add_two_numbers(num1, num2, num3, num1, num2, num3, num1, num2, num3, num1, num2, num3)
# print(result)

###
# age = int(input("What is your age ? "))
# has_NIC = eval(input("Do you have a NIC ? "))

# if age >= 25:
#     print("You are allowed")

# elif has_NIC==True:
#     print("You are allowed")
# else:
#     print("You are underaged")
###
#What is list?#
#4/01/2024#
# names = ["Muaz", "Taimoori", 23, 40000, "male", True]
# len_of_names = len(names)
# for index in range(len_of_names):
#     print(names[index])

###
#markshit
# students_data = [
#     ['Ali', 'Akbar', 80, 65, 100],
#     ['Ahmed', 'Akbar', 70, 100, 46],
#     ['Hamza', 'Ahmed', 4, 70, 35],
#     ['Tasawwar', 'Yousuf', 100, 85, 30],
#     ['Bisma', 'Azam', 100, 100, 100],
#     ['Zain', 'Javed', 80, 40, 37],
#     ]
# total_marks = 100
# passing_marks = 50
# for data in students_data:
#     name = data[0]
#     fname = data[1]
#     maths_marks = data[2]
#     physics_marks = data[3]
#     sindhi_marks = data[4]
#     total_marks_obtained = sum([maths_marks, physics_marks, sindhi_marks])
#     percentage = (total_marks_obtained / total_marks) * 100
#     if maths_marks >= passing_marks and physics_marks >= passing_marks and sindhi_marks >= passing_marks:
#         result = 'Passed'
#     else:
#         result = 'Failed'
#         print(name, "name of", fname, "has", result, "with total numbers", total_marks_obtained)
#         print(name, "has scored percentage =", percentage)
###
#List# #useless#

# lst = [
#     'Zain', 'Ahmed', [60, 70, 61] , 300
# ]

# lst = [
#     'Zain', 'Ahmed', 3 , 300
# ]
# '''
# while condition:
#     do something
#     update condition - monitor - change 
# '''

# no_of_students = int(input("How many students in your classroom ? "))
# for i in range(no_of_student):
# n = 0
# while n < no_of_students:
#     name = input(f"What is your {n+1}th student name ?? ")
#     fname = input(f"What is your {n+1}th student's father name ?? ")
#     number_of_subjects = int(input("How many subjects attempted ?? "))
#     total_marks = input("what are the total marks ?? ")
#     subject_marks = []
#     subject_marks.append(arguments)
#     if number_of_subjects > 0:
#         print("Please insert your marks subject wise...!")
#         for i in range(number_of_subjects):
#             temp = int(input("State your marks here"))
#             subject_marks.append(temp)
#     temp_lst = [name, fname, subject_marks, total_marks]
#     lst_of_students_data.append(temp_lst)
#     n= n + 1

# print(lst_of_students_data)
###
no_of_students = int(input("How many students in your class ? "))
'''
while condition:
    do something
    update condition - monitor - change
'''
sample_lst = [[
    'Zain', 'Ahmed', [60, 70, 61] , 300
],
[
    'Amjad', 'Asfar', [60, 70, 61] , 300
]
]
n = 0
lst_of_students_data = []
while n < no_of_students:
    name = input(f"What is your {n+1}th student name ??")
    fname = input(f"What is your {n+1}th student's father name ??")
    number_of_subjects = int(input("How many subjects attempted ??"))
if number_of_subjects == 0:
    print(temp = 0)
    total_marks = int(input("what are the total marks ??"))
    subject_marks = []
    # subject_marks.append(arguments)
    if number_of_subjects > 0:
        print("Please insert your marks subject wise..! ")
        for i in range(number_of_subjects):
            temp = int(input("State your marks here .. "))
            subject_marks.append(temp)
    temp_lst = [name, fname, subject_marks, total_marks]
    lst_of_students_data.append(temp_lst)     
    n = n + 1

print(lst_of_students_data)

###
# no_of_students = int(input("How many students in your class ? "))
# '''
# while condition:
#     do something
#     update condition - monitor - change
# '''
# sample_lst = [[
#     'Zain', 'Ahmed', [60, 70, 61] , 300
# ],
# [
#     'Amjad', 'Asfar', [60, 70, 61] , 300
# ]
# ]
# n = 0
# lst_of_students_data = []
# while n < no_of_students:
#     name = input(f"What is your {n+1}th student name ??")
#     fname = input(f"What is your {n+1}th student's father name ??")
#     number_of_subjects = int(input("How many subjects attempted ??"))
# if number_of_subjects == 0:
#     print(temp = 0)
#     total_marks = int(input("what are the total marks ??"))
#     subject_marks = []
#     # subject_marks.append(arguments)
#     if number_of_subjects > 0:
#         print("Please insert your marks subject wise..! ")
#         for i in range(number_of_subjects):
#             temp = int(input("State your marks here .. "))
#             subject_marks.append(temp)
#     temp_lst = [name, fname, subject_marks, total_marks]
#     lst_of_students_data.append(temp_lst)     
#     n = n + 1

# print(lst_of_students_data)

#Project Frizz Bizz# ODD/EVEN
# num = int(input ("Enter any number: "))
# if (num % 2) == 0: 
#     print ("Fizz") 
# else: 
#     print ("Buzz")
#Dictionary#
# st1_dict = {"name":"zain", "fname":"Javed",}
# st2_dict = {"fname": "Sultan","name":"Zainab"}
# st3_dict = {"fname":"Sultan", "name":"Zainab","Class":8}

# for i in st3_dict:
#     print(i, st3_dict{i})
###Dictionary###
# student_strenght = int(input("how many student ?"))
# std_1st = []
# for _ in range(student_strenght) :
#     std_data = dict()
#     name = input("what is your name ?")
#     fname = input("what is your fname ?")
#     age = int(input("what is your age ?"))
#     std_data['name'] = name
#     std_data['fname'] = fname
#     std_data['age'] = age
#     std_1st.append(std_data)
#     print(std_1st)
###FILING/file handling###
# # """
# # a = dict()
# # {'key' : value}

# # """
# # salary = 'salary'
# # student1 = {
# #     "name": "Ali", 'age' : 18, salary: 18000, 'school': None
# # }

# # student2 = {
# #     'age' : 18, "name": "Ali", salary: 18000, 'school': None
# # }
import json
# list 
# dictionaries -> string " " | Should be in double quotation
# Strings
student_strength = int(input("How many students ? ")) # 3
std_lst = []
for _ in range(student_strength): # 3
    std_data = dict() # { }
    name = input("Enter name ?") 
    fname = input("Enter fname ?") 
    age = input("Enter age ?")
    std_data['name'] = name 
    std_data['fname'] = fname 
    std_data['age'] = age 
    std_lst.append(std_data)
# a+ read and append
# json.dumps -> json readable bnadeta ha data ko
str_data = json.dumps(std_lst)
file = open('student_data.json', 'w+')
json_data = json.dumps(std_lst) 
file.write(json_data)

file = open('student_data.txt', 'w+')
file.write(str(std_lst))

file_txt = open('student_data.txt', 'r')
file_json = open('student_data.json', 'r')


a = file_txt.read()
b = file_json.read()
# print(type(a), type(b))
formatted_data = json.loads(b)
print(type(formatted_data))

print(len(formatted_data))
print(formatted_data[1]['name'])
# # print(file_txt.read(), "< Text File")
a = file_txt.read()
# print(file_json.read(), "< JSON File")
b = file_json.read()

# json.loads file se code readable data read hota ha
# data_a = json.loads(a)
data_b = json.loads(b)
print(data_b)
print(data_b[0]['name'])
print(data_b[0]['fname'])
print(data_b[0]['age'])
# print(type(a))
# print(type(b))
# print(json.loads(b.decode("utf-8")))
# print(json.loads(a))


