started = False
stoped = False
while True:
    user = input("> ")
    if user.lower() == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")

    elif user == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...Ready to go!")

    elif user == "stop":
        if stoped:
            print("Car is already stoped!")
        else:
            stoped = False
            print("Car stopped.")
    
    elif user == "quit":
        quit()
    else:
        print("I don't understand that...")