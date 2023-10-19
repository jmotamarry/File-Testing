def search(searchInput):
    file = open("test", "r")
    for line in file:
         if searchInput in line:
            print(line)
def add():
    file = open('test', 'a')
    file.write("\n")
    file.write(input('Type New Content'))



while True:
    firstInput = input('Type "Search", "Add", or "Close"')
    if firstInput == 'Search' or firstInput == 'search':
        search(input('Type Search Query'))
        continue
    elif firstInput == 'Add' or firstInput == 'add':
        add()
        print('Successfully Added')
        continue
    elif firstInput == 'Close' or firstInput == 'close':
        print('Successfully Closed')
        break
    else:
        print('Please choose "Search", "Add", or "Close"')
        continue