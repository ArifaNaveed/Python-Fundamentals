import json
from datetime import datetime

customers_message = [
    { "name" : "abc" , "message" : "I want to track my order status" },
    { "name" : "plu" , "message" : "I want to ask products you have" } ,
    { "name" :  "alia" , "message" : "I want to refund my order" } , 
    { "name" : "noone" , "message" : "" }
]


def ordered_list(filtered):

    highlist = []
    medlist = []
    lowlist = []
    mylist = []

    for vals in filtered:

        if (vals["priority"] == "high"):
            highlist.append(vals)
    
        elif (vals["priority"] == " medium"):
            medlist.append(vals)

        else:
            lowlist.append(vals)
        
    mylist = highlist + medlist + lowlist

    print("Sorted List : ")
    print(json.dumps(mylist, indent=4))



def check_priority(customers):
    customers_filter = {}
    filtered = []

    for msg in customers:

        if (not msg["message"].strip()):
            print("Empty String by", msg["name"])
            continue

        customers_filter = {}
        value = msg["message"]

        customers_filter["name"] = msg["name"]
        customers_filter["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if ("order" in value or "refund" in value or "payment" in value or "track" in value or "change" in value):
            customers_filter["priority"] = "high"
            customers_filter["message"] = value

        elif ("password" in value or "login" in value or "probelm" in value):
            customers_filter["priority"] = "medium"
            customers_filter["message"] = value


        else:
            customers_filter["message"] = value
            customers_filter["priority"] = "low"
        
        filtered.append (customers_filter)
       
    ordered_list(filtered)

def __main__():
    check_priority(customers_message)


__main__()
        


