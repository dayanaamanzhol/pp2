#ex1
class strings:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())

m = strings()
m.getString()
m.printString()

#ex2
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

shape = Shape()
print(shape.area())  

square = Square(5)
print( square.area())  

#ex3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(5, 9)
print(rectangle.area())  

#ex4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

point1 = Point(1, 2)
point2 = Point(4, 6)

point1.show()  
point2.show()  

point1.move(3, 5)
point1.show()  

distance = point1.dist(point2)
print(distance)  

#ex5
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} accepted. Balance is {self.balance}.")
        else:
            print("Error")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} accepted. Balance is {self.balance}.")
        else:
            print("Error")


account = BankAccount("Alice")
print(f"{account.owner}: {account.balance}")

account.deposit(100)
account.withdraw(50)
account.withdraw(70)  
account.deposit(-100)

#ex6
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n)):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print(prime_numbers)
