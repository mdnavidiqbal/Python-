# # 1. Problem-Variable Swap: Write a Python program to swap the values of two variables without using a temporary variable.
# x = 5
# y = 6 
# x,y = y,x
# print("X : ",x)
# print("Y : ",y)

# # 2. Problem-Even or Odd: Write a Python program that takes an integer as input and prints whether it is even or odd.
# n = int(input("Enter any number : "))
# if n % 2 == 0 : 
#     print("Even")
# else : 
#     print("Odd")

# # 3.Problem-String Reverse:  String Reverse: Write a Python function to reverse a given string and return the reversed string.
# name = "navid"
# reversed_string = name[::-1]
# print(reversed_string)


# # 4.Problem-Type Conversion: Given a list of integers, write a Python program to convert each element of the list to a string.

# roll_list = [1,2,3,4,5]
# string_list = []
# for element in roll_list:
#     string_list.append(str(element))
# print("Original List : ",roll_list)
# print("Converted List : ",string_list)

# # 5.Problem-Temperature Converter: Write a Python program that converts a temperature in Celsius to Fahrenheit. Take the Celsius temperature as input from the user.

# C = int(input("Enter any tmeperature : "))
# Fahrenheit = ((C*9)/5)+32
# print("The temperature is : ",Fahrenheit)

# # 6.Write a Python function that takes a variable as input and returns the data type of the variable as a string (e.g., “int”, “float”, “str”, “list”, etc.).

# def check_type(varibale):
#     print(type(varibale))

# print(check_type(10))
# print(check_type(10.5))
# print(check_type("10"))
# print(check_type([1,2,3]))


# # 7.String Palindrome: Write a Python function to check if a given string is a palindrome or not.
# Given_string = "Madam"
# s = Given_string.lower()
# rev_string = s[::-1]
# if s == rev_string:
#     print("The string is palindrom")
# else:
#     print("The string is not palindrom")

# # 8. String Reversal with Slicing: Write a Python function to reverse a given string using slicing.

# def rev_strig(x):
#     print(x[::-1])

# rev_strig(x = input("Enter the string : ")

# # 9.Write a Python program that takes two strings as input and concatenates them into a single string without using the `+` operator.
# def concat_string(str1,str2):
#     return ''.join([str1,str2])

# str1 = input("Enter the first string : ")
# str2 = input("Enter the second string : ")
# result = concat_string(str1,str2)
# print("The concte string is : ",result )

# # 10. Typecasting Challenge: Given three variables: `a = ‘100’`, `b = 25`, and `c = ‘10.5’`, write a Python program to perform the following operations and print the results: – Convert `a` to an integer and add it to `b`. – Convert `c` to a float and subtract it from the result of the first operation. – Convert the final result to a string and concatenate it with the string ” is the answer.”
# a = 100
# b = 25 
# c = 10.5
# A = int(a) 
# Add = A + b 
# print("Add of a and b is : ",Add)
# C = float(c)
# Substract = Add - C 
# print("The substract of Add and c is : ",Substract)
# convert_string = str(Substract)
# print(type(convert_string))
# str = "is the answer"
# concate = ''.join([convert_string,str])
# print("The final result is : ",concate)


# #11. Positive, Negative, or Zero: Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.
# def check_number(n):
#     if n > 0:
#         print("The number is positive")
#     elif n < 0 : 
#         print("The number is negative")
#     elif n == 0 : 
#         print("The number is zero ")
#     else:
#         print("The number is wrong")
# n = int(input("Enter any number : "))
# check_number(n)

# #12. Largest of Three Numbers: Write a Python program that takes three numbers as input and prints the largest among them.

# def large_number(a,b,c):
#     if a>b and a>c:
#        largest = a 
#     elif b>a and b>c : 
#         largest = b
#     else:
#         largest = c
#     return largest
# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))
# c = int(input("Enter the third number : "))
# L = large_number(a,b,c)
# print(f"The largest number among {a},{b},{c} is : {L}")

# # 13. Leap Year Checker: Write a Python program that takes a year as input and determines if it is a leap year or not.
# def check_LeapYear(y):
#     if (y % 4 == 0 and y % 100  != 0) or y % 100 != 0 :
#         print("Leap year")
#     else:
#         print("Not leap year")
# y = int(input("Enter any year : "))
# check_LeapYear(y)

# # 14. Grades Classification: Write a Python program that takes a student’s percentage as input and prints their corresponding grade according to the following criteria: – 90% or above: A+ – 80-89%: A – 70-79%: B – 60-69%: C – Below 60%: Fail
# def check_grade(num):
#     if (num >=90):
#         print("A+")
#     elif (num >= 80):
#         print("A")
#     elif(num >= 70):
#         print("B")
#     elif(num >= 60):
#         print("C")
#     else:
#         print("F")
# num = float(input("Enter the number : "))
# check_grade(num)

