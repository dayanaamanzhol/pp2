#ex1
import functools
a = [1, 2, 3, 4, 5]
print(functools.reduce(lambda x, y: x * y, a))

#ex2
s = str(input())
low = 0
up = 0
for i in s:
    if i.islower():
        low +=1
    if i.isupper():
        up +=1
print("lower case:", low, "upper case:", up)

#ex3
s = str(input())
t = s[::-1]
if t == s:
    print("palindrome")
else:
    print("not palindrome")

#ex5
a = (True, True, False)
b = (True, True, True)
print(all(a))
print(all(b))
