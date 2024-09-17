#intializing dictionary.
student_grade={ }
#add function.
def add_student(name,grade):
    student_grade[name]=grade
    print(f"Added {name} with a {grade}")


#udate function
def update_student(name,grade):
    if name in student_grade:
        student_grade[name]=grade
        print(f"the {name} grade {grade}is updated")
    else:
        print(f"{name} is not found")

    #Delete function

def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} is successfully deleted.")
    else:
        print(f"{name} is not found.")


#Display function
def display_all_students():
    if student_grade:
        for name,grade in student_grade.items():
            print(f"{name}:{grade}")
    else:
        print("data can not found")


#main logic
def main():
    while True:
        print("\nstudent grade management oprations.")
        print("1.Add student")
        print("2.Update student")
        print("3.delete student")
        print("4.Display student")
        print("5.Exit program")
        choice=int(input("Enter the your choice:"))
        if choice == 1:
            name=input("Enter the name:")
            grade=int(input("Enter the grade:"))
            add_student(name,grade)
        elif choice == 2:
            name=input("Enter the name:")
            grade=int(input("Enter the grade:"))
            update_student(name,grade)

        elif choice == 3:
            name=input("Enter the name:")
            delete_student(name)
        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("exit the program.")
            break
                                    
        else:
            print("invalid choice")
if __name__ == "__main__":
    main()
