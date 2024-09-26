#ToDo List Starter Phrase.
td_list = []
print("")
print("")
print("")
print("Welcome to the ToDo Tracker!")
print("--------------------------------------------")
print("")
print("")


#While loop to loop the ToDo list.
while 1:
    print("Your current ToDos are: ")
    print("~~~~~~~~~~")
    print("")
    #For loop cycles through list contents to add a number next to them and list them vertically.
    num = 0
    for x in td_list:
        num = num + 1
        print(str(num) + ") " + str(x))
    print("~~~~~~~~~~")
    print("")
    print("")
    #Asks to add or remove a list item.
    print("Would you like to add or remove an item?")
    print("~~~~~~~~~~")
    choice = str(input("Enter Choice: "))
    print("~~~~~~~~~~")
    print("")
    print("")


    #Choices.
        #Adds an item to the list.
    if choice.lower() == "add":
        print("What would you like to add to your ToDo list?")
        print("~~~~~~~~~~")
        add = str(input("Enter: "))
        print("~~~~~~~~~~")
        td_list.append(add)
        print("")
        print("Added.")
        print("~~~~~~~~~~")
        print("--------------------------------------------")
        print("")

        #Removes an item from the list.
    elif choice.lower() == "remove":
        print("What number item would you like to remove from your ToDo list.")
        print("~~~~~~~~~~")
        remove = int(input("Enter Number: "))
        print("~~~~~~~~~~")
        del td_list[remove - 1]
        print("")
        print("Removed.")
        print("~~~~~~~~~~")
        print("--------------------------------------------")
        print("")

        #If error encountered.
    else:
        print("")
        print("Sorry I do not understand. Please try again.")
        print("~~~~~~~~~~")
        print("--------------------------------------------")
        print("")