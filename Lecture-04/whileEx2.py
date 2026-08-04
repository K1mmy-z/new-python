keep_going = 'y'
while keep_going == 'y':
    items = float(input('Enter the item wholesale cost :'))
    price = items * 2.5
    print(f'Retail price ${price:.2f}')
    keep_going = input('Do you have another item' + \
                       '(Enter y for yes) : ')