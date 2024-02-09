#ex1
def ounces(grams):
    print(grams * 28.3495231)

g = int(input())
ounces(g)

#ex2
def conversion(F):
    print((5/9) * (F - 32))

f = int(input())
conversion(f)

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

#ex9 
def volume(radius):
    print((4/3) * 3.14 * radius * radius * radius)

r = int(input())
volume(r)

#ex10 
def unique_list(nums):
    unique = []
    for i in nums:
        if i not in unique:
            unique.append(i)
    return unique
    
numbers = input()
numbers = numbers.split()
print(unique_list(numbers))

#ex11
def palindrome(str):
    t = str[::-1]
    if t == str:
        print("Yes")
    else:
        print("No")
    
s = input()
palindrome(s)

#ex12
def histogram(nums):
    for x in nums:
        print('*' * int(x))
    
numbers = input()
numbers = numbers.split()
histogram(numbers)

#ex13
import random
def play():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name},I am thinking of a number between 1 and 20.")

    number = random.randrange(1, 20)
    guesses = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            break

    print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
    
play()
