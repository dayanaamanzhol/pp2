#ex1
n = int(input())

def gen_sqr(n):
    for i in range(n):
        yield i*i


a = gen_sqr(n)
for i in a:
    print(i)
