#help, start, stop, quit

started = False
user_input = ""

print("Welcome to Car Game!")
print(f'''Press any key to continue.)
or help to view the commands.
''')

while True:
    user_input = input(": ").lower()
    if user_input == 'help':
        print('''
help - shows this text
start - starts the engine
stop - stops the engine
quit - terminates this program
''')
    elif user_input == 'start':
        if started:
            print("Engine already running.")
        else:
            started = True
            print("Engine started.")
    elif user_input == 'stop':
        if not started:
            print("Engine is not running.")
        else:
            started = False
            print("Engine stopped.")
    elif user_input == 'quit':
        print("Terminating program...")
        break
    else:
        print("Input invalid.")

# gad this shit is challenging
