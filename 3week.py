##############      Functions         ##############
#def printlength(city):
#    print(len(city), city, end = " ")


#cities = ["lahore", "multan", "mardan", "delhi", "london"]
#actors = ("asd dg", "shk", "hakjn hs", "uwjh")

#printlength(actors)
#printlength(cities)

##########################################################

#lists: list[str] = ["apple", "banana", "mango", "grapes"]

#def printlistelements(list):
#    print("Inside Function")
#    for items in list:
#        print(items, end=" ")

#printlistelements(lists)

##########################################################



#def factorial(variable):
#    fact = 1
#    for x in range(1,variable+1):
#        fact *= x
#    return fact

#x = int(input("Enter a number : "))
#result = factorial(x)
#print("Factorial of", x, "is =", result)

##########################################################


#def PKR(dollar):
#    print("Inside Function")
#    rupee = dollar * 278
#    print("Dollars in PKR are :", rupee)

#PKR(12)


##########################################################


#def whetherevenorodd(number):
#    if (number%2 == 0):
#        print("Even")
#    else:
#        print("Odd")

#number = int(input("Enter a number : "))
#whetherevenorodd(number)


##########################################################

##############      RECURSION        ##############

#def fact(n):
#    if (n == 1):
#        return 1
#    else:
#        return n * fact(n-1)
    
#print(fact(5))

##########################################################


#def sumfornumbers(num):
#    if (num == 0):
#        return 0
#    else:
#        return sumfornumbers(num-1) + num
    
#nums = int(input("enter number : "))
#print(sumfornumbers(nums))

##########################################################


def listprinter(list,idx=0):
    if (idx == len(list)):
        return
    else:
        print (list[idx]) 
        listprinter(list, idx+1)

lists = ["sara", "ali", "sana", "hafsa"]
listprinter(lists)