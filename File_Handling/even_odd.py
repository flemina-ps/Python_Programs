a=[]
e=[]
o=[]
a1=int(input("Enter the number of elements in list : "))
for i in range(0,a1):
    a2=input(f"Enter the element {i+1} in list_1 : ")
    a.append(a2)
    if i%2==0:
        e.append(i)
    else:
        o.append(i)

even="even.txt"
odd="odd.txt"
with open(even,"w") as e:
    print("Even numbers are: ")





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
