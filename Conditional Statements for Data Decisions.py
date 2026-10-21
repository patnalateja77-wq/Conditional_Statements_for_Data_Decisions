# Conditional Statements for Data Decisions

# 1. Positive or Negative Number
num = 10
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

# 2. Even or Odd
num = 7
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# 3. Pass or Fail
marks = 75
if marks >= 35:
    print("Pass")
else:
    print("Fail")

# 4. Grade Classification
marks = 85
if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 35:
    print("Grade C")
else:
    print("Fail")

# 5. Voting Eligibility
age = 23
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

# 6. Find the Largest Number
a = 25
b = 40
if a > b:
    print("A is Greater")
elif b > a:
    print("B is Greater")
else:
    print("Both are Equal")

# 7. Temperature Classification
temperature = 32
if temperature >= 35:
    print("Hot Weather")
elif temperature >= 20:
    print("Moderate Weather")
else:
    print("Cold Weather")

# 8. Multiple Conditions Using AND
age = 23
has_id = True
if age >= 18 and has_id:
    print("Entry Allowed")
else:
    print("Entry Not Allowed")

# 9. Multiple Conditions Using OR
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Working Day")

# 10. Employee Salary Classification
salary = 45000
if salary < 25000:
    print("Low Salary")
elif salary <= 50000:
    print("Medium Salary")
else:
    print("High Salary")

# 11. Student Attendance Eligibility
attendance = 80
if attendance >= 75:
    print("Eligible for Examination")
else:
    print("Not Eligible for Examination")

# 12. Discount Calculation
purchase_amount = 2500
if purchase_amount >= 3000:
    discount = 0.20
elif purchase_amount >= 2000:
    discount = 0.10
else:
    discount = 0

discount_amount = purchase_amount * discount
final_amount = purchase_amount - discount_amount

print("Purchase Amount:", purchase_amount)
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)

# 13. Student Performance Classification
students = {
    "Ravi": 92,
    "Kiran": 78,
    "Priya": 65,
    "Arun": 30,
    "Sneha": 85
}

for name, marks in students.items():
    if marks >= 90:
        result = "Excellent"
    elif marks >= 75:
        result = "Good"
    elif marks >= 35:
        result = "Pass"
    else:
        result = "Fail"

    print(name, "-", marks, "-", result)
