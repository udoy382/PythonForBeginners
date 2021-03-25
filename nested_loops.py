# adding one loop into another loop

# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")


# Exercise Solutions

numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for x_count in numbers:
    # print('X' * x_count)

    output = ''
    for count in range(x_count):
        output += 'X'
    print(output)