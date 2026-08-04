col = int(input('How many column?'))
for i in range(1,101):
    print(f"{i:>3}", end=" ")
    if i % col == 0:
        print()