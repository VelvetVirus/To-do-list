to_do_lst = []
running = True

while running:
    user_act = input('What would you like to do? (show/add/delete/modify/exit) ').lower()

    if user_act == 'show':
        print(to_do_lst)

    elif user_act == 'add':
        add_running = True  # Flag to control the "add" loop
        while add_running:
            user_inp = input('Please enter your task: (to stop adding tasks write "n") ')

            if user_inp == 'n':
                add_running = False  # Set the flag to exit the "add" loop
            else:
                to_do_lst.append(user_inp)

    elif user_act == 'delete':
        print(to_do_lst)
        to_do_lst.remove(input('What would you like to delete?' ))
        

    elif user_act == 'modify':
        print(to_do_lst)

        ele_to_modify = input('What would you like to modify? ')
        new_value = input('What would you like to switch it with? ')
    
        if ele_to_modify in to_do_lst:
            index = to_do_lst.index(ele_to_modify)
            to_do_lst[index] = new_value
            print('Modified list: ', to_do_lst)
        else:
            print('Element not found in the list. No modification made.')

    elif user_act == 'exit':
        running = False  # Exit the main loop when "exit" is entered

    else:
        print('Invalid choice. Please enter a valid option.')
