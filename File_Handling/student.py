filename="student_details.txt"
with open(filename,"w") as file:
    n=int(input("Enter the number of students : "))
    for i in range(1,n+1):
        print(f"Enter the details of student {i}")
        name=input("Name : ")
        age=int(input("Age : "))
        grade=input("Grade : ")
        file.write(f"Student {i} \n")
        file.write(f"Name : {name}\n")
        file.write(f"Age : {age}\n")
        file.write(f"Grade : {grade}\n")
        file.write("-"*20 + "\n")

print(f"Student details have been written to {filename}")

