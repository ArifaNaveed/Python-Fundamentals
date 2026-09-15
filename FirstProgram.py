##########################   Day 1st   ########################## 
print("Hello World!", "My name is this")
print(23)
print(23*34)
price = 90.99
name = 'Arifa'
age = 23
print("My name is:",name,"My age is:",age,"The price is:",price) 

##########################   Day 2nd   ########################## 
print(type(name))
print(type(age))
print(type(price))
aa = None
old = False
print(type(aa), type(old))

a = 5
b = 9
sum = a+b
print("sum is:",sum)
sum+=sum
print("sum after +=", sum)
sum*=2
print("Sum after *= is:", sum)


## logical operators   ##
all = True
ball = False
print(not True)
print(not False)
print("Are all and ball both true?", all and ball)
print("Is anyone of all and ball true?", all or ball)

###  Type Conversion  ###
age1 = 23
age2 = 3.45
print(age1+age2)   # convert age1 to float to match type of age2 that is type conversion automatic

# type casting manually
alim = 3.23
alim = str(alim)  # a is now string not integer
print(type(alim))



##########   Input from user   #########
# input("Enter your Name:")  take input from user also prints a message but not stored in a variable here

name = int(input("Enter your age"))  # by deafault type of name is string so to change type we have to use type casting
print("You entered:", name,"Data Type:",type(name))


##### Practice Questions  #####
# take 2 number input from user and print their sum

num1 = int(input("Enter Number 1"))
num2 = int(input("Enter number 2"))
sum = num1 + num2
print("Sum of your entered numbers is:",sum)

# take sides of square as input from user and print its area

side = int(input("Enter square's one side length:"))
area = side*side   # side ** 2
print("Area of square is: ",area)

# two floating point numbers from user and print their average
first = float(input("Enter a decimal number"))
second = float(input("Enter another decimal number"))
avg = (first+second)/2
print("Average is : ", avg)

### last task
print("Num1 and Num2: ",num1>=num2)
