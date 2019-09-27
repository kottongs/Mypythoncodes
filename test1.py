command = ""
started = False
while True:
    command = input('> ').lower()
    if command =='start':
        if started:
            print('car is alredy started')
        else:
            started = True
            print('car started...')
    elif command == 'help':
        print("""
1. type quit to quit
2. type start to start
3.  type help for help
        """)
    elif command == 'stop':
        if not started:
            print('car is already stopped')
        else:
            started = False 
            print('car stopped...')
    elif command == 'quit':
        break
    else:
        print("I don't understand you...") 