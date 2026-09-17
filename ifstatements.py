###########  If Statements   ###########

temp = 30
temp = int(input("Enter Temperature:"))
if temp > 30:
    print ("Hot Weather")
else:
    print ("Cold Weather")


score = int(input("What is your score:"))
if score >= 90:
    print ("A+")
elif score>= 80:
    print ("A")
else:
    print ("Fail")


age = int(input("What's your age:"))
if age >= 18:
    country = input("Enter your country:").capitalize()
    if country == "Pakistan":
        print ("Eligible for Voting")
    else:
        print ("Not Eligible in Pakistan")
else:
    print ("Under age")


if age >= 18 and country == "Pakistan":
    print ("Eligible in Pakistan")
else:
    print ("Not Eligible")


###########  My Practice Task  ###########
print("Enter 3 Subject Marks out of 100:-")
score1 = int(input())
score2 = int(input())
score3 = int(input())
print ("Done")
result1 = score1+score2+score3
print ("You scored:",result1)
result = (result1/300)*100
print ("Percentage:",result)
if result >= 90:
    print ("A+")
elif result >= 80:
    print ("A")
elif result >= 70:
    print ("B")
elif result >= 60:
    print ("C")
else:
    print ("Failed!")