def add_items():
    '''
    This function adds items to the list
    '''
    print("What do you want to add to the list? ")
    add_list = input("Add list: ")
    to_do_list.append(add_list)
    return to_do_list
def view_list():
    '''
    this function allows the user to view the list
    '''
    if len(to_do_list) == 0:
        print("The list is empty, there is nothing to view.")
    else:
        print(to_do_list)
def remove_items():
    '''
    this function allows the user to remove items from the list
    '''
    if len(to_do_list) == 0:
        print("The list is empty, there is nothing to remove.")
    else:
        while True:
            print("What do you want to remove from the list?")
            remove_list = input("Remove from the list:")
            if remove_list in to_do_list:
                to_do_list.remove(remove_list)
                return
            elif remove_list == "":
                print("That is an invalid input try again. ")
            else:
                print("That item is not in the list try again.")

to_do_list = []
while True:
    print("Please enter 'add', 'view', 'remove' or 'quit'.")
    user_input = input("Do you want to add items, remove items, view your list or quit the program :").lower()

    if user_input == "add":
        add_items()
    elif user_input == "view":
        view_list()
    elif user_input == "remove":
        remove_items()
    elif user_input == "quit":
        quit()
    else:
        print("That was an invalid input")

    print(f"This is the updated list: {to_do_list}")