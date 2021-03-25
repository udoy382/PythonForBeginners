try:
    age = int(input("Enter you age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("age cannot be 0")
except ValueError:
    print("Invalid value")