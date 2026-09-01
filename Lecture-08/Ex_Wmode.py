def example__plus_mode():
    with open('example_w+.txt','w+') as file:
        file.write("This is the first line in the file.\n")
        file.write("This is the second line in the file.\n")
        file.seek

        content = file.read()
        print("Content of the file after writing:")
        print(content)
        
example__plus_mode()