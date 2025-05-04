students={}

def add_student():
    name=input("Enter student name: ")
    subjects={}
    for subject in ["Math","Seience","English"]:
        score=float(input(f"Enter marks for {subject}:"))
        subjects[subject]=score
    students[name]=subjects
    print(f"Student {name} added successfully!")

def view_report():
    name=input("Enter student name to view report:")
    record=students.get(name)
    if record:
        total=sum(record.values())
        average=total/len(record)
        grade=get_grade(average)
        print(f"Report for {name}:")
        for subject, mark in record.items():
            print(f"{subject}: {mark}")
        print(f"Average: {average}")
        print(f"Grade: {grade}")
    else:
        print(f"No record found for {name}.")

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"
    
def delete_student():
    name=input("Enter student name to delete:")
    if name in students:
        del students[name]
        print(f"Student {name} deleted successfully!")
    else:
        print(f"No record found for {name}.")

def update_score():
    name=input("Enter student name to update score:")
    if name in students:
        subject = input("Enter subject to update:")
        if subject in students[name]:
            new_score=float(input(f"Enter new score for {subject}:"))
            students[name][subject]=new_score
            print(f"Score for {subject} updated successfully!")
        else:
            print(f"No record found for {subject} in {name}'s report.")
    else:
        print(f"No record found for {name}.")

def menu():
    while True:
        print("\nStudent Report Card Manager")
        print("1. Add Student")
        print("2. View Report")
        print("3. Delete Student")
        print("4. Update Score")
        print("5. Exit")
        
        choice=input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_report()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            update_score()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")

menu()

