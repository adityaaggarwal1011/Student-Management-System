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
    user_input = input("enter the unique ID to be removed: ") 
    with open("students.csv","r+") as file:
        lines = csv.reader(file)
        for line in lines:
            if line[0] == user_input:
                lines.remove(line)
                break
        










if __name__ == "__main__":
    main()