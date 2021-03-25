number = 9

x = 0
y = 3
z = 1

try:
    while x < y:
        print(f"Your total chnace is 3. counted your try {z}")
        z +=1
        user = int(input("Enter the number: "))
        x +=1
        if user > 9:
            print("Oops! wrong number. [ it's too big] try again...")
        elif user < 9:
            print("Oops! wrong number. [it's too small] try again...")
        else:
            print("Congratulations! you own :)")
            break
except Exception as e:
    print("Sorry! your entered is wrong. please wright input!")