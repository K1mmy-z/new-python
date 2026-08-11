fruits_with_duplicate = ['apple','banana','apple', 'cherry','apple','kiwi']
while 'apple' in fruits_with_duplicate:
    fruits_with_duplicate.remove('apple')
print(f'Fruit after remove :{fruits_with_duplicate}')