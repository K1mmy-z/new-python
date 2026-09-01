def exampel_a_plus_mode():
    with open('example_a+.txt','a+') as file:
        file.seek(0)

        content = file.read()
        print("Current content of the file: ")
        print(content)

        file.write("Appendding a new line to the file.\n")
        file.seek(0)
        updated_content = file.read()
        print("\nUpdated content of the file:")
        print(updated_content)

exampel_a_plus_mode()