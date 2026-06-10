import csv
def main():
    print("Hello, Welcome to project\n","STUDENT MANAGEMENT SYSTEM")

#Getting the data from csv
def get_data():
    students = []
    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"ID":row["ID"],
                            "Name":row["Name"],
                            "Age":row["Age"],
                            "Gender":row["Gender"],
                            "Contact":row["Contact"],
                            "Class":row["Class"]
    })
    return students


#Adding new student to csv
def add_data():
    new_student = input("Enter the following:\nID, Name, Age, Gender, Contact, Class\n")
    with open("students.csv","a") as file:
        file.write(new_student)


#Deleting a student from csv
def delete_data():
    students = get_data()
    delete_id = input("Enter ID to delete: ")
    for student in students:
        if student["ID"] == delete_id:
            students.remove(student)
            break
    
    with open("students.csv", "w", newline="") as file:
        fieldnames = ["ID", "Name", "Age", "Gender", "Contact", "Class"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)





#Find by ID
def find_by_id():
    students = get_data()
    unique_id= input("Enter the unique ID: ")
    for student in students:
        if student["ID"] == unique_id:
            print(student)
            break

#Find by name
def find_by_name():
    students = get_data()
    unique_name= input("Enter the unique name: ")
    for student in students:
        if student["Name"] == unique_name:
            print(student)
    
#Find by class
def find_by_class():
    students = get_data()
    grade= input("Enter the class: ")
    for student in students:
        if student["Class"] == grade:
            print(student)
    

#Sort by age
def sort_by_age():
    students = get_data()
    students.sort(key=lambda student: int(student["Age"]))    
    for student in students:
        print(student, "\n".strip())


#Sort by name
def sort_by_name():
    students = get_data()
    students.sort(key=lambda student: student["Name"])  
    for student in students:
        print(student, "\n".strip())

#Sort by class
def sort_by_class():
    students = get_data()
    students.sort(key=lambda student: int(student["Class"]))    
    for student in students:
        print(student, "\n".strip())











if __name__ == "__main__":
    main()