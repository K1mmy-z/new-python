with open('employee.txt', 'r') as emp_file:
    for line in emp_file:
        print(f'Name: {line.strip()}')
        print(f'ID: {emp_file.readline().strip()}')
        print(f'Department: {emp_file.readline().strip()}')