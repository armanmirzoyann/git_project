command = ""
started = False
while True :
    command = input("> ").lower()
    if command == "start":
        if started :
            print("Car is Already started ")
        else :
            started = True
            print("Car Started...")
    elif command == "stop":
        if not started :
            print("Car is Already Stopped ")
        else :
            started = False
            print("Car stoped...")
    elif command == "help":
        print("""
start - to start
stop - to stop
quit - to quit
                """)
    elif command == "quit" :
        break
else:
    print("Sory!!!! I don't understand...")