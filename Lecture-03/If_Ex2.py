score1 = int(input("Enter the score for test:"))
score2 = int(input("Enter the score for test:"))
score3 = int(input("Enter the score for test:"))
numScore = (score1 + score2 + score3) / 3
print("the average score is ",format(numScore,".1f"))
if numScore > 95:
    print("Cogratulations")