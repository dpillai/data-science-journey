#variables - just give things names

name = "Sam"
age = 25
price = 19.99

#print stuff
print (f" Hello {name}")

#lists - collection of thing
todos = ["small", "medium", "large"]
todos.append("x-large")
first_item = todos[0]
print(f"first item is {first_item}")

#If statements
if age >= 18:
    print("Adult")
else:
    print("Minor")

#loops

for item in todos:
    print(f"item is {item}")

#Functions - name code you want to name

def greet(person):
    return f"Hi {person}!"

message = greet(name)

print(message)