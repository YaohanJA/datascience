
#  File: Day.py

#  Description: Day of the week, given a year


year = eval(input("Enter year: "))
while (year<1900) or (year>2100):
    year = int(input("Enter year:"))

month = eval(input("Enter month: "))
while (month<1) or (month>12):
    month = eval(input("Enter month: "))

day = eval(input("Enter day: "))

if year%400 !=0 and month ==2:
        while (day<1) or (day>28):
          day = eval(input
                     
                     ("Enter day: "))
        
elif year%400 ==0 and month ==2:    
        while (day<1) or (day>29):
          day = eval(input("Enter day: "))
        
else:
    while (day<1) or (day>31):
        day = eval(input("Enter day: "))

if month < 3:
    year = year -1
    
if month > 2:
    month = month -2
else:
    month = month +10
    


a=month
b=day
c=year%100
    
d = year//100

w = (13 * a - 1 ) // 5 

x = c // 4 

y = d // 4 

z = w + x + y + b + c - 2 * d 

r = z % 7 

r = (r + 7) % 7

list = ["Sunday", "Monday", "Tuesday","Wednesday", "Thursday", "Friday", "Saturday"]

print("The day is", list[r])
    
    
