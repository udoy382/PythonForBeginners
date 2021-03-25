# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print("move")

#     def draw(self):
#         print("draw")

# point = Point(10, 20)
# # point.x = 11
# print(point.x)

# Exercise Solutions

class Perosn:
    def __init__(self, name):
        self.name = name

    def takl(self):
        print(f"Hi I am {self.name}")

x = Perosn("Saifur Rahman Udoy")
# print(x.name)
x.takl()
bob = Perosn("Bob Smith")
bob.takl()