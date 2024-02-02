#ex1
def ounces(grams):
    print(grams * 28.3495231)

g = int(input())
ounces(g)

#ex2
def conversion(F):
    print((5/9) * (F - 32))

f = int(input())
conversion(Fahrenheit)

#ex3
def solve(numheads, numlegs):
    rabbits = (numlegs - 2*numheads)/2
    chikens = numheads - rabbits
    print(int(rabbits), "Rabbits")
    print(int(chikens), "chikens")
    
heads = 35
legs = 94
solve(heads, legs)

#ex4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = []
    for x in numbers:
        if is_prime(int(x)):
            prime_numbers.append(int(x))
    return prime_numbers

numbers = input()
numbers = numbers.split()
print(filter_prime(numbers))

#ex5
s = str(input())
def permutation(st):
    t = ""
    for x in st:
        if x != " ":
            t = t + x
    print(t)

permutation(s)

#ex6
def reverse(st):
    st = st[::-1]
    words = st.split()
    t = ""
    for word in words:
        word = word[::-1]
        t = t + word + " "
        
    print(t)

s = str(input())
reverse(s)

#ex7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] == '3':
            return True
    return False

numbers = input()
numbers = numbers.split()
print(has_33(numbers))

#ex8
def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == '0' and nums[i+1] == '0' and nums[i+2] == '7':
            return True
    return False

numbers = input()
numbers = numbers.split()
print(spy_game(numbers))

