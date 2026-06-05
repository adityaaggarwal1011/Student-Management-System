import csv
def main():
    delete_data()




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



def add_data():
    new_student = input("Enter the following:\nID, Name, Age, Gender, Contact, Class\n")
    with open("students.csv","a") as file:
        file.write(new_student)


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





if __name__ == "__main__":
    main()