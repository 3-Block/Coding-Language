while True:
    command = input(' >>> ')
    if command.startswith('say('):
        if command.endswith(')'):
            print(command[4:][:-1])
        else:
            print('Function not closed')
    elif command == '':
        print('',end='')
    else:
        print(command)
        for letter in command:
            print('^',end='')
        print('')
        print('"' + command + '"' + ' is not defined')