command = ''
started = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Car is already started...')

        else:
            started = True
        print('Car started...')
    elif command == 'stop':
        print('Car stopped...')
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - quit
        ''')
    elif command == "quit":
        print("Stopping the command")
        break

    else:
        print('Sorry we do not support this command')




