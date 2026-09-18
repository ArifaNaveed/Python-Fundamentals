#############    LOOPS       ###########

#############      WHILE    LOOPS       ###########

tup1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0
value = False
x = int(input("Enter the value to find in my tuple : "))
while i < len(tup1):
  if (x == tup1[i]):
     print(tup1[i], "is at", i+1, "location in tuple")
      value = True
 i += 1
 if(not value):
  print(x, "not found in my tuple")

#######################################################



#############   FOR   LOOPS       ###########
tup1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter value : "))

for vals in tup1:
   if (x == vals):
       print(x, "found")
       break
else:
   print("Loop Completes")

######################################################

n = int(input("Enter number : "))
for num in range(1,11):
   print(n, "x", num, "=", num*n)


for num in range(0,10):
   pass    # use in exception handling to display nothing so no error by interperter


#######################################################


i = 1
sum = 0
x = int(input("Enter a number : "))
while i <= x:
    sum += i
    i += 1

print("LOOP COMPLETES AND SUM IS : ",sum)


#######################################################
###############   SAME  CODE (Previous)  WITH   DIFFERENT   LOOP     ###############

sum = 0
for vals in range(1,x+1):
    sum += vals
else:
    print("LOOP COMPLETES AND SUM IS : ",sum)


#######################################################

x - int(input("Enter a number : "))
fact = 1
for value in range(x,0,-1):
    fact *= value

print("Loop ends and factorial of", x, "is : ", fact)
