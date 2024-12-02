#Create a contact card
contact={}
while True:
    choice=int(input("\n 1.Add a contact \n 2.Delete a contact \n 3.Edit a contact \n 4.Search a contact \n 5.List all contacts \n 6.Exit \n Enter your choice : "))
    if choice==1:
        name=input("Name : ")
        phone=input("Phone No.")
        contact[name]=phone
    elif choice==2:
        del_contact=input("Enter the contact to be deleted : ")
        if del_contact in contact:
            contact.pop(del_contact)
            print("Name \t\t Contact Number ")
            for key in contact:
                print(f"{key}\t\t{contact.get(key)}")
        else:
            print("No contact found!")
    elif choice==3:
        edit_contact=input("Enter the contact to be edited : ")
        if edit_contact in contact:
            phone=input("Enter the phone number : ")
            contact[edit_contact]=phone
            print("Contact updated")
            print("Name \t\t Contact Number ")
            for key in contact:
                print(f"{key}\t\t{contact.get(key)}")
        else:
            print("No contact found!")
    elif choice==4:
        search_contact=input("Enter the contact to be searched : ")
        if search_contact in contact:
            print(search_contact,"'s contact number is",contact[search_contact])
        else:
            print("No contact found!")
    elif choice==5:
        if not contact:
            print("Contact book is empty!")
        else:
            print("Name \t\t Contact Number ")
            for key in contact:
                print(f"{key}\t\t{contact.get(key)}")
    else:
        break