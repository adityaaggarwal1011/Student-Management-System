import csv
def main():
    get_data()
    add_data()








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





















if __name__ == "__main__":
    main()