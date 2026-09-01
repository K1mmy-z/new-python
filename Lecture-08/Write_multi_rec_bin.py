import struct

num_records = int(input("How many records do you want to create? "))

with open("records.bin", "wb") as file:
    for _ in range(num_records):
        record_id = int(input("Enter record ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gpa = float(input("Enter GPA: "))
        
        # Pack the data into binary format
        data = struct.pack('i20sif', record_id, name.encode('utf-8'), age, gpa)
        file.write(data)

print(f"{num_records} records have been written to records.bin.")