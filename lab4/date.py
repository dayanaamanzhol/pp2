#ex1
import datetime
x = datetime.datetime.today().date() - datetime.timedelta(days = 5)
print(x)

#ex2
y = datetime.datetime.today().date() - datetime.timedelta(days = 1)
t = datetime.datetime.today().date() 
tm = datetime.datetime.today().date() + datetime.timedelta(days = 1)
print("yesterday", y)
print("today", t)
print("tomorrow", tm)

#ex3
x = datetime.datetime.now()
time = x.replace(microsecond=0)
print(time)

#ex4
import datetime
def difsec(date1, date2):
    dt1 = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")

    diff = (dt2 - dt1).total_seconds()
    return diff


date1 = input("Enter date1 (YYYY-MM-DD HH:MM:SS): ")
date2 = input("Enter date2 (YYYY-MM-DD HH:MM:SS): ")

dif = difsec(date1, date2)
print(abs(dif))
