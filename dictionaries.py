'''

customer = {
    "name":"Saifur Rahman Udoy",
    "age":30,
    "is_verified":True
}

customer["birthdate"] = "1 oct 2003"
print(customer.get("namet", "jan 1 2003"))
print(customer["birthdate"])

'''
# Exercise Solutions

phone = input("Enter the number: ")

digit = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five"
}

output = " "
for ch in phone:
    output += digit.get(ch, "!" + " ")
print(output)