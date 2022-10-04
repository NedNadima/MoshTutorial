command = ""
running = False

while True:
    command = input('> ').lower()
    if command == 'start':
        if running == True and command == 'start':
            print('Car is already started!')
        else:
            print('The car is starting')
            running = True

    elif command == 'stop':
        if running == True and command == 'stop':
            print('Stopping the car!')
            running = False
        else:
            print('The car is already stopped')
            running = False
    elif command == 'help':
        print('''
Type Start to start the car
Type Stop to stop the car
Type Quit to quit the car
        ''')
    elif command == 'quit':
        print('Quitting game, sorry to see you go!')
        break
    else:
        print("Sorry we don't speak americano")
