####################    FILE INPUT OUTPUT      ######################
#with open("practice.txt", "w") as file:
#    data = "Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java."
#    file.write(data)

#with open("practice.txt", "w") as file:  
#    new_data = data.replace("Java", "Python")
#    file.write(new_data)    


#def checkforword(word):
#    with open("practice.txt", "r") as file: 
#        data = file.read()
#        if(data.find(word)):
#            print("Found")

#def checkline(word):
#    with open("practice.txt", "r") as file: 
#        data1 = file.readline()
#        data2 = file.readline()
#        data3 = file.readline()
#        data4 = file.readline()
#        data5 = file.readline()

#        if(data1.find(word) != -1):
#            print("Found at line 1")
        
#        elif(data2.find(word) != -1):
#            print("Found at line 2")

#        elif(data3.find(word)!= -1):
#            print("Found at line 3")

#        elif(data4.find(word) != -1):
#            print("Found at line 4")

#        elif(data5.find(word) != -1):
#            print("Found at line 5")

#        else:
#            print ("Word not Found")


#def check_line(word):
#    with open("practice.txt", "r") as file: 
#        data = True
#        lineno = 1
#        while data:
#            data = file.readline()
#            if (word in data):
#                print("Found at", lineno, "Line")
#                return
#            lineno += 1
#        return -1

#check_line("learning")
#checkline("no")
#checkforword("learning")    


#######################################################################


#with open("practice.txt", "r") as file:
#    data = file.read()
#    print(data)

#    even = " "
#    for items in range(len(data)):
#        if(data[items] == ","):
#            even = int(even)
#            if(even%2 == 0):
#                print(even, "Even")
#            else:
#                print(even, "Odd")
#            even = ""
#        else:
#            even += data[items]


#######################################################################


with open("practice.txt", "r") as my:
    data = my.read()
    nums = data.split(",")

    for num in nums:
        if(int(num)% 2 == 0):
            print(num, "Even")
        else:
            print(num, "Odd")