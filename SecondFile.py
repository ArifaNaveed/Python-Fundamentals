###############   LISTS AND TUPLES IN PYTHON      ###############   

movies = []
movies.append(input("Enter 1st movie : "))
movies.append(input("Enter 2nd movie : "))
movies.append(input("Enter 3rd movie : "))
print(movies)

#####################################################

tup = (3,"ali",9)     # tuple can also have different data type
print(type(tup))

#####################################################

###############  Palindrome Lists      ###############
print("This program will check either the list is palindrome or not")   
mylists = []
mylists.append(input("Enter 1st element"))
mylists.append(input("Enter 1st element"))
mylists.append(input("Enter 2nd element"))
mylists.append(input("Enter 3rd element"))

#####################################################


mylist = mylists.copy()
mylist.reverse()
if(mylist == mylists):
   print("Palindrome List")
else:
   print("non-Palindrome List")

#####################################################

grades = ["C","D","A","A","B","B","A"]
grades.sort()
print("List in ascending order : ", grades)

####################   Dictonaries and Sets    ####################
dic1 = {
    "table" : ["a peice of furniture", "lists of facts & figures"] ,
    "cat" : "a small animal" 
}
print(dic1)

#####################################################

classroom = {"Python", "Java", "C++", "C", "JavaScript"}    # set 
print("Total Number of classrooms required for these students : ",len(classroom))
print(type(classroom))

#####################################################

marks = {}
x = int(input("Enter Chemistry marks : "))
y = int(input("Enter Physics marks : "))
z = int(input("Enter Maths marks : "))

marks.update({"chem" : x})
marks.update({"phy" : y})
marks.update({"maths" : z})
print(marks)

#####################################################

sets = {8, "8.0"}
print(sets)

