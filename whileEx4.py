import random

print('What is my magic number (1 to 100) ? ')
mynumber = random.randint(1,100)
ntrie = 1
yourguess = -1
while ntrie < 7 and yourguess != mynumber:
    msg = str(ntrie) + ">>"
    if (ntrie == 6) :
        print("Your last chance")
    yourguess = int(input(msg))
    if yourguess > mynumber:
        print("--> too high")
    if yourguess < mynumber:
     print("--> too low")
    ntrie += 1
if yourguess == mynumber:
    print("Yes it's" ,mynumber)
else:
    print("Sorry! MY number is ", mynumber)