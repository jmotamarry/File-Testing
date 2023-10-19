def search(query):
    file = open("schoolFilerInformation", "r")
    for line in file:
        if query in line:
            print(line)


def add(add_input):
    while True:
        file = open('schoolFilerInformation', 'a')
        confirmation = (input(add_input + ' - Do you want to add this? Type "Yes" or "No"')).lower()
        if confirmation == 'yes':
            file.write("\n")
            file.write(add_input)
            print('Successfully Added')
            break
        elif confirmation == 'no':
            break
        else:
            print('Invalid Input')
            continue
    continuation = input("Continue Adding? Type yes or no").lower()
    if continuation == 'yes':
        add(input('Type New Content'))
    elif continuation == 'no':
        return
    else:
        print('Invalid Input')


def display_all():
    file = open('schoolFilerInformation', 'r')
    for line in file:
        print(line)


def which_function():
    while True:
        first_input = (input('Type "Search", "Add", "Show all", or "Close"')).lower()
        if first_input == 'search':
            search(input('Type Search Query'))
            continue
        elif first_input == 'add':
            add(input('Type New Content'))
            continue
        elif first_input == 'close':
            print('Successfully Closed')
            break
        elif first_input == 'show all':
            display_all()
        else:
            print('Invalid Input')
            continue


which_function()
