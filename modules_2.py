# def lbs_to_kg(weight):
#     return weight * 0.45

# def kg_to_lbs(weight):
#     return weight / 0.45

# Exercise Solutions

def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = numbers
    return maximum