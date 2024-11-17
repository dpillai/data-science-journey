#save data
with open('notes.txt', 'w') as file:
    file.write("meeting at 3 am \nCall John")

#read data
with open('notes.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())