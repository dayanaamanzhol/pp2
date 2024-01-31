#ex1
def ounces(grams):
    print(grams * 28.3495231)

ounces(grams)

#ex2
def conversion(F):
    print((5/9) * (F - 32))

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
num = [1, 2, 3, 4, 5]
def filter_prime(n):


for x in num:
    filter_prime(x)

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
def spy_game(nums):
    


spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 