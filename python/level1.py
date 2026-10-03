# Que 1
number=int(input("Enter the number:"))

if number%2==0:
    print("even")
else:
    print("odd")    

# Que 2
a = int(input("Enter the number a"))
b = int(input("Enter the number b"))

if a>b:
    print(f"number a is greater:",a)
else :    
    print(f"number b is greater:",b)

# Que 3 
a = int(input("Enter the number a"))
b = int(input("Enter the number b"))
c = int(input("Enter the number c")) 

if a>b or a>c:
    print(f"number a is greater a",a)
elif b>a or b>c:
    print(f"number a is greater b",b)  
else:      
    print(f"number a is greater c",c) 

# Que 4
number = int(input("Enter a number:"))

if number>0:
    print("Positive")
elif number<0:
    print("Negative")
elif number == 0:
    print("ZERO")
else :
    print("Invalid input")

#Que 5
age = int(input("Enter your age:"))

if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age >= 20:
    print("Adult")
else :
    print("Invalid input")

# Que 6
marks = int(input("Enter your marks:"))

if marks>=90 and marks<=100:
    print("A")
elif marks>=80 and marks<90:
    print("B")
elif marks>=70 and marks<80:
    print("C")
elif marks>=60 and marks<70 :
    print("D")
elif marks>=0 and marks<60:
    print("F")
else :
    print("Invalid input")    

#Que 7
number = int(input("Enter a number:"))

if number%5 == 0:
    print("Divisible by 5")
elif number %5 != 0:
    print("Not Divisible by 5")
else :
    print("Invalid input")

# Que 8
number = int(input("Enter a number:"))

if number%3 == 0 and number %5 == 0:
    print("Divisible by both 3 and 5")
elif number %3 != 0 and number %5 == 0:
    print("Divisible by 5 but not by 3")
elif number %3 ==0 and number %5 != 0:
    print("Divisible by 3 but not by 5")
elif number %3 != 0 and number %5 != 0:
    print("Not Divisible by both 3 and 5")
else :
    print("Invalid input")

# Que 9 
year = int(input("Enter a number of year:"))

if year%400 == 0 or year%4 == 0:
    print("Leap year")
elif year %400 != 0 or year%4 != 0:
    print("Odd")
else :
    print("Invalid input")

# Que 10           
number = int(input("Enter a number:"))

if number >= 10 and number<=50:
    print("In range of 10 to  50")
else :
    print("Out of range")