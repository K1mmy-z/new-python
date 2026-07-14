weight = int(input("Enter your weight in kilogram: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height * height)
print("Your BMI is : ",format(bmi,".2f"))

if bmi < 18.5:
    print("UNDERWEIGHR")
elif 18.5>=bmi<=24.9:
    print("NORMAL")
