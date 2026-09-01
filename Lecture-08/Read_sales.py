with open('sale.txt', 'r') as sale_file:
    line = sale_file.readline()
    while line != '':
        amount = float(line)
        print(format(amount, '.2f'))
        line = sale_file.readline()