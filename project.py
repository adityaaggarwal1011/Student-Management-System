with open("student.txt","r") as file:
    lines= file.readlines()

for line in lines:
    print(line.rstrip())

print(type(lines))