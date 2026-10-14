
# ============================================================
# PYTHON IF-ELIF-ELSE PRACTICE PROGRAMS
# Total Questions: 30
# ============================================================


# Q1. Check whether a number is positive, negative, or zero.

n = float(input("Q1. Enter a number: "))

if n > 0:
    print("Positive number")
elif n < 0:
    print("Negative number")
else:
    print("Zero")


# ============================================================
# Q2. Check whether a number is even or odd.
# ============================================================

n = int(input("\nQ2. Enter an integer: "))

if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# ============================================================
# Q3. Find the greater of two numbers.
# ============================================================

a = float(input("\nQ3. Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("Greater number:", a)
elif b > a:
    print("Greater number:", b)
else:
    print("Both numbers are equal")


# ============================================================
# Q4. Find the greatest of three numbers.
# ============================================================

a = float(input("\nQ4. Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest number:", a)
elif b >= a and b >= c:
    print("Greatest number:", b)
else:
    print("Greatest number:", c)


# ============================================================
# Q5. Check whether a person is eligible to vote (age >= 18).
# ============================================================

age = int(input("\nQ5. Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# ============================================================
# Q6. Check whether a year is a leap year.
# ============================================================

year = int(input("\nQ6. Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# ============================================================
# Q7. Check whether a character is a vowel or consonant.
# ============================================================

ch = input("\nQ7. Enter an alphabet: ").lower()

if len(ch) != 1 or ch not in "abcdefghijklmnopqrstuvwxyz":
    print("Invalid alphabet")
elif ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")


# ============================================================
# Q8. Check whether a number is divisible by 5 and 11.
# ============================================================

n = int(input("\nQ8. Enter a number: "))

if n % 5 == 0 and n % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")


# ============================================================
# Q9. Check whether a number is a multiple of both 3 and 7.
# ============================================================

n = int(input("\nQ9. Enter a number: "))

if n % 3 == 0 and n % 7 == 0:
    print("Multiple of both 3 and 7")
else:
    print("Not a multiple of both 3 and 7")


# ============================================================
# Q10. Assign grades based on marks.
# 90-100: A, 80-89: B, 70-79: C, 60-69: D, Below 60: F
# ============================================================

marks = float(input("\nQ10. Enter marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")


# ============================================================
# Q11. Check whether a character is uppercase or lowercase.
# ============================================================

ch = input("\nQ11. Enter a character: ")

if len(ch) != 1 or not ch.isascii() or not ch.isalpha():
    print("Enter a single English alphabet")
elif ch.isupper():
    print("Uppercase")
else:
    print("Lowercase")


# ============================================================
# Q12. Check whether an alphabet is a vowel using if-elif.
# ============================================================

ch = input("\nQ12. Enter an alphabet: ").lower()

if len(ch) != 1 or ch not in "abcdefghijklmnopqrstuvwxyz":
    print("Invalid alphabet")
elif ch == "a":
    print("Vowel")
elif ch == "e":
    print("Vowel")
elif ch == "i":
    print("Vowel")
elif ch == "o":
    print("Vowel")
elif ch == "u":
    print("Vowel")
else:
    print("Consonant")


# ============================================================
# Q13. Check whether three sides can form a triangle.
# ============================================================

a = float(input("\nQ13. Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid side lengths")
elif a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Cannot form a triangle")


# ============================================================
# Q14. Determine the type of triangle.
# Equilateral, Isosceles, or Scalene.
# ============================================================

a = float(input("\nQ14. Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid side lengths")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


# ============================================================
# Q15. Find the largest among four numbers.
# ============================================================

a = float(input("\nQ15. Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("Largest number:", a)
elif b >= a and b >= c and b >= d:
    print("Largest number:", b)
elif c >= a and c >= b and c >= d:
    print("Largest number:", c)
else:
    print("Largest number:", d)


# ============================================================
# Q16. Check whether a number is a three-digit number.
# ============================================================

n = int(input("\nQ16. Enter an integer: "))

if 100 <= abs(n) <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")


# ============================================================
# Q17. Calculate electricity bill using sample slab rates.
# First 100 units: Rs. 1.50/unit
# Next 100 units: Rs. 2.50/unit
# Above 200 units: Rs. 4/unit
# ============================================================

units = float(input("\nQ17. Enter electricity units: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 1.50
    print("Electricity bill: Rs.", bill)
elif units <= 200:
    bill = 100 * 1.50 + (units - 100) * 2.50
    print("Electricity bill: Rs.", bill)
else:
    bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4
    print("Electricity bill: Rs.", bill)


# ============================================================
# Q18. Calculate income tax using illustrative income slabs.
# Up to Rs. 3,00,000: 0%
# Rs. 3,00,001-6,00,000: 5% above Rs. 3,00,000
# Rs. 6,00,001-10,00,000: Rs. 15,000 + 10% above Rs. 6,00,000
# Above Rs. 10,00,000: Rs. 55,000 + 20% above Rs. 10,00,000
# ============================================================

income = float(input("\nQ18. Enter annual taxable income: "))

if income < 0:
    print("Invalid income")
elif income <= 300000:
    tax = 0
    print("Income tax: Rs.", tax)
elif income <= 600000:
    tax = (income - 300000) * 0.05
    print("Income tax: Rs.", tax)
elif income <= 1000000:
    tax = 15000 + (income - 600000) * 0.10
    print("Income tax: Rs.", tax)
else:
    tax = 55000 + (income - 1000000) * 0.20
    print("Income tax: Rs.", tax)


# ============================================================
# Q19. Check whether a student passes all subjects.
# Minimum 35 marks in each subject.
# ============================================================

m1 = float(input("\nQ19. Enter subject 1 marks: "))
m2 = float(input("Enter subject 2 marks: "))
m3 = float(input("Enter subject 3 marks: "))

if not all(0 <= m <= 100 for m in (m1, m2, m3)):
    print("Invalid marks")
elif m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Student passes")
else:
    print("Student fails")


# ============================================================
# Q20. Check whether a number is within a given range.
# Range: 10 to 100, inclusive.
# ============================================================

n = int(input("\nQ20. Enter a number: "))

if 10 <= n <= 100:
    print("Number is within the range")
else:
    print("Number is outside the range")


# ============================================================
# Q21. Build a simple calculator using if-elif-else.
# Operations: Addition, Subtraction, Multiplication, Division.
# ============================================================

a = float(input("\nQ21. Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


# ============================================================
# Q22. Check whether a year is a century leap year.
# A century year is a leap year only if divisible by 400.
# ============================================================

year = int(input("\nQ22. Enter a year: "))

if year % 100 == 0 and year % 400 == 0:
    print("Century leap year")
elif year % 100 == 0:
    print("Century year, but not a leap year")
elif year % 4 == 0:
    print("Leap year, but not a century year")
else:
    print("Not a leap year")


# ============================================================
# Q23. Determine the season based on the month number.
# Example classification for the Northern Hemisphere.
# ============================================================

month = int(input("\nQ23. Enter month number (1-12): "))

if month < 1 or month > 12:
    print("Invalid month")
elif month in (3, 4, 5):
    print("Spring")
elif month in (6, 7, 8):
    print("Summer")
elif month in (9, 10, 11):
    print("Autumn")
else:
    print("Winter")


# ============================================================
# Q24. Find the number of days in a month.
# February depends on whether the year is a leap year.
# ============================================================

month = int(input("\nQ24. Enter month number (1-12): "))
year = int(input("Enter year: "))

if month < 1 or month > 12 or year < 1:
    print("Invalid month or year")
elif month in (1, 3, 5, 7, 8, 10, 12):
    print("31 days")
elif month in (4, 6, 9, 11):
    print("30 days")
elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("29 days")
else:
    print("28 days")


# ============================================================
# Q25. Check whether a password meets minimum conditions.
# At least 8 characters, one digit, uppercase and lowercase.
# ============================================================

password = input("\nQ25. Enter password: ")

has_digit = any(ch.isdigit() for ch in password)
has_upper = any(ch.isupper() for ch in password)
has_lower = any(ch.islower() for ch in password)

if len(password) < 8:
    print("Password must contain at least 8 characters")
elif not has_digit:
    print("Password must contain a digit")
elif not has_upper:
    print("Password must contain an uppercase letter")
elif not has_lower:
    print("Password must contain a lowercase letter")
else:
    print("Password meets the conditions")


# ============================================================
# Q26. Determine ticket price based on age category.
# Sample ticket prices.
# ============================================================

age = int(input("\nQ26. Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket price: Rs. 0")
elif age <= 17:
    print("Ticket price: Rs. 100")
elif age <= 59:
    print("Ticket price: Rs. 200")
else:
    print("Ticket price: Rs. 120")


# ============================================================
# Q27. Calculate discount based on purchase amount.
# Below Rs. 1,000: 0%
# Rs. 1,000-4,999: 5%
# Rs. 5,000-9,999: 10%
# Rs. 10,000 and above: 20%
# ============================================================

amount = float(input("\nQ27. Enter purchase amount: "))

if amount < 0:
    print("Invalid purchase amount")
else:
    if amount < 1000:
        discount = 0
    elif amount < 5000:
        discount = amount * 0.05
    elif amount < 10000:
        discount = amount * 0.10
    else:
        discount = amount * 0.20

    print("Discount: Rs.", discount)
    print("Final amount: Rs.", amount - discount)


# ============================================================
# Q28. Check driving licence eligibility.
# Practice conditions: age >= 18 and satisfactory eyesight.
# ============================================================

age = int(input("\nQ28. Enter your age: "))
eyesight = input("Is eyesight satisfactory? (yes/no): ").lower()

if age < 0:
    print("Invalid age")
elif eyesight not in ("yes", "no"):
    print("Invalid eyesight response")
elif age >= 18 and eyesight == "yes":
    print("Eligible to apply")
else:
    print("Not eligible under these conditions")


# ============================================================
# Q29. Create a basic login system.
# Sample credentials: student / Python123
# ============================================================

correct_username = "student"
correct_password = "Python123"

username = input("\nQ29. Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful")
elif username != correct_username:
    print("Incorrect username")
else:
    print("Incorrect password")


# ============================================================
# Q30. Create a menu-driven calculator.
# Options: Addition, Subtraction, Multiplication, Division, Exit.
# ============================================================

while True:
    print("\n========== CALCULATOR MENU ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a + b)

    elif choice == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a - b)

    elif choice == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a * b)

    elif choice == "4":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")

    elif choice == "5":
        print("Exiting calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1 to 5.")


# ============================================================
# END OF ALL 30 PYTHON PROGRAMS
# ============================================================
