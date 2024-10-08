#Creating contact dictionary.
contact = dict()

#Loop.
while 1:
    #Menu
    print("Contact Book")
    print()
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. List Contacts")
    print("4. Exit")
    print()
    choice = input("Enter choice number: ")
    print()

    #Choice options.
    #Add contact.
    if choice == "1":
        print()
        name = input("Enter contact name: ")
        print()
        num = input("Enter contact number: ")
        #Check if phone number is valid.
        while 1:
            try:
                int(num)
            except:
                print()
                print("Not a valid number.")
                print("Try again.")
                print()
                num = input("Enter contact number: ")
                continue
            else:
                if len(num) != 10:
                    print()
                    print("Not a valid number.")
                    print("Try again.")
                    print()
                    num = input("Enter contact number: ")
                    continue
                else:
                    break
        print()
        #Add Contact.
        contact[name] = num
        print("Contact added.")
        print()
        print()
    
    #Remove contact.
    elif choice == "2":
        print()
        name = input("Enter name of person you want to remove: ")
        print()
        #Check if contact exists to remove.
        while 1:
            try:
                del contact[name]
            except:
                print("Person does not exist in contacts.")
                print("Try again.")
                print()
                name = input("Enter name of person you want to remove: ")
                continue
            else:
                break
        print("Contact removed.")
        print()
        print()

    #List contacts.
    elif choice == "3":
        print()
        print("Contacts:")
        print()
        for x in contact:
            print(str(x) + ": " + str(contact[x]))
        print()
        print()

    #Exiting program.
    elif choice == "4":
        print()
        print("Exiting program.")
        break

    #Error encountered.
    else:
        print()
        print("Sorry I do not understand.")
        print("Please try again.")
        print()
        print()