age = int(input("Enter your age:"))
income = float(input("Enter your Income:"))

if age >= 18 and age <= 65 and income > 30000:
    print("you are eligible for the loan")
else:
    print("you are not eligible for the loan")