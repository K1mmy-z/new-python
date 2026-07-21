score = int(input("Enter a test core :"))

while score < 0 or score >100:
    print("Error: The score cannot be nagative")
    print("or greater than 100.")
    score = int(input("Enter the correct score: "))