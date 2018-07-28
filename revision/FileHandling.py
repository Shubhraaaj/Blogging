arr = [26,12,19,95, 22, 1, 19, 99]

file1 = open("example.txt", "w")
file2 = open("example.txt", "r")
file3 = open("example.txt", "a")

file1.write("Hello Programmer, Welcome to Python!\n\n")
nameStr = "Enter your name: "
ageStr = "Enter your age: "
inpStatus = 1

while(inpStatus == 1):
    name = input(nameStr)
    age = input(ageStr)
    file3.write("Name: " + name + "\nAge: " + age + "\n\n")
    inpStatus = int(input("Thank you for entering the details.\n1. Input new data\n2. Exit the program\n"))

content = file2.readlines()
for i in content:
    print(i.strip())

file1.close()
file2.close()
file3.close()