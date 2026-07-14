hours = int(input("Enter the number of hours worked: "))
rate = int(input("Enter the the hourly pay rate: "))
pay = hours * rate

if hours > 40:
    pay = (40 * rate) + ((hours - 40) * (rate * 1.5))

print("The gross pay is : $",format(pay,".2f"))