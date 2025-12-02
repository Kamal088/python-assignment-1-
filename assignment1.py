#Task 1:
# Name: Kamal Prajapati
# Roll No: 2501660048
# Course: BCA
# Semester: 1st
# Subject: Problem Solving with Python
# Assignment: Unit-1 Mini Project
# Title: Student Profile Console App
# Date: 2024-12-19

print("=" * 50)
print("WELCOME TO STUDENT PROFILE CONSOLE APPLICATION")
print("=" * 50)
print("This tool helps students create their academic profile")
print("using Python programming basics.")
print()

#Task 2: Input & Variables
print("Please enter your details:")
print("-" * 30)

# Student information inputs
student_name = input("Enter your full name: ")
roll_number = input("Enter your roll number: ")
program = input("Enter your program: ")
university_name = input("Enter your university name: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))  # Type conversion to int
hobby = input("Enter your hobby: ")

print("\n" + "=" * 50)
print("OPERATORS DEMONSTRATION")
print("=" * 50)

# Task 3: Operators Demonstration
print("\n--- Operators Demonstration ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Arithmetic Operators
print(f"\nArithmetic Operators:")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")
print(f"{num1} // {num2} = {num1 // num2}")

# Assignment Operators
print(f"\nAssignment Operators:")
x = num1
print(f"Original x = {x}")
x += num2
print(f"After x += {num2}: x = {x}")
x -= num2
print(f"After x -= {num2}: x = {x}")

# Comparison Operators
print(f"\nComparison Operators:")
print(f"{num1} > {num2} = {num1 > num2}")
print(f"{num1} < {num2} = {num1 < num2}")
print(f"{num1} == {num2} = {num1 == num2}")
print(f"{num1} != {num2} = {num1 != num2}")

# Logical Operators
print(f"\nLogical Operators:")
print(f"({num1} > 10) and ({num2} < 20) = {(num1 > 10) and (num2 < 20)}")
print(f"({num1} > 10) or ({num2} < 20) = {(num1 > 10) or (num2 < 20)}")
print(f"not({num1} > 10) = {not(num1 > 10)}")

# Identity Operators
print(f"\nIdentity Operators:")
print(f"num1 is num2 = {num1 is num2}")
print(f"num1 is not num2 = {num1 is not num2}")

# Membership Operators
print(f"\nMembership Operators:")
sample_list = [1, 2, 3, 4, 5]
print(f"Sample list: {sample_list}")
print(f"{int(num1)} in sample_list = {int(num1) in sample_list}")
print(f"{int(num1)} not in sample_list = {int(num1) not in sample_list}")

print("\n" + "=" * 50)
print("STRING OPERATIONS")
print("=" * 50)

# Task 4: Python Strings & Formatting
print("\n--- String Operations ---")

# String Concatenation
full_intro = "Hello " + student_name + "! Welcome to " + university_name
print(f"String Concatenation: {full_intro}")

# f-strings
f_string_demo = f"Student: {student_name}, Roll No: {roll_number}, Age: {age}"
print(f"f-string Example: {f_string_demo}")

# Escape Characters
print("\nEscape Characters:")
print("This is a tab\t-> see the space")
print("This is on line 1\nThis is on line 2")
print("He said: \"Python is awesome!\"")
print('She replied: \'Yes, it is!\'')

# String Methods
print("\nString Methods:")
print(f"Original Name: {student_name}")
print(f"Upper Case: {student_name.upper()}")
print(f"Lower Case: {student_name.lower()}")
print(f"Title Case: {student_name.title()}")
print(f"Strip Demo: '{'   hello   '.strip()}'")
print(f"Replace 'a' with '@': {student_name.replace('a', '@')}")
print(f"Count 'a' in name: {student_name.count('a')}")
print(f"Length of name: {len(student_name)}")

print("\n" + "=" * 50)
print("FINAL STUDENT PROFILE")
print("=" * 50)
