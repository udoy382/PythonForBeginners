while True ==x:
    print("You have 3 chance for guess the hidden number: ")
    user = int(input("Enter the number: "))
    if user > 9:
        print("Oops! wrong number. [ it's too big] try again...")
    elif user < 9:
        print("Oops! wrong number. [it's too small] try again...")
    else:
        print("Congratulations! you own :)")