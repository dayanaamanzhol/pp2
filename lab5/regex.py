import re
#ex1

txt = input()
x = re.search("ab*", txt)
if x:
    print("matched")
else:
    print("not matched")
 
 
#ex2
 
txt = str(input())
x = re.match("a(bbb?)", txt)
if x:
    print("matched")
else:
    print("not matched")
 
#ex3
 
txt = str(input())
x = re.findall("[a-z]+_", txt)
print(x)
 
#ex4
 
txt = str(input())
x = re.findall("[a-z]+[A-Z]", txt)
print(x)
 
#ex5
 
txt = str(input())
x = re.match("a.*b$", txt)
if x:
    print("matched")
else:
    print("not matched")
   
#ex6
 
txt = str(input())
x = re.sub("\s|[,]|[.]", ":", txt)
print(x)
 
#ex7
 
txt = input()
x = re.sub("_([a-z])", lambda x: x.group(1).upper(), txt)
print(x)
 
#ex8
 
txt = input()
x = re.findall("[A-Z][^A-Z]*", txt)
print(x)
 
#ex8
 
txt = input()
x = re.findall("[A-Z][^A-Z]*", txt)
print(x)
 
#ex9
 
txt = input()
x = re.sub("([A-Z])", r" \1", txt)
print(x)
 
#ex10
 
txt = input()
x = re.sub("([a-z])([A-Z])", r"\1_\2", txt)
print(x.lower())

file = open("row.txt", "r", encoding= "utf-8")
print(file.readlines())
