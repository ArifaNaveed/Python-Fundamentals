#################   FIRST PROJECT   #############
# import random 

# def rollthedice(dice):
#     dice1 = random.randint(1,6)
#     dice2 = random.randint(1,6)

#     if (dice == 2):
#         print(f'({dice1}, {dice2})')

#     else:
#         print(f'({dice1})')

    



# def __main__():
#     print("Game Started")
#     count = 0
    
#     while (True):
#         dice = int(input("How many dice? (1,2) "))
#         if (not (dice == 1 or dice == 2)):
#             print("Only 2 dice available")
#         else:
#             break
            
#     while (True):

#         print("\nRoll the DIce (y/n)")
#         choice = input("Choice : ").lower()

#         if (choice == "y"):
#             rollthedice(dice)
#             count += 1
    
#         elif (choice == "n"):
#             print("Thanks For Playing!")
#             break

#         else:
#             print("Invalid Choice")

#     print("\nYou rolled", count, "dices in this session")
        


# __main__()

#####################   SECOND PROJECT   ####################


# import random

# def __main__():
#     print("##########   Guess the correct number between 1 and 100   ##########")
    
#     num = random.randint(1,100)

#     while True:
#         try:
#             user_num = int(input("Enter your number : "))
#         except ValueError:
#             print("Enter a valid number")
#             continue

#         if (user_num >= 0 and user_num <= 100):
#             if (user_num > num):
#                 print("Too High")

#             elif (user_num < num):
#                 print("Too Low")

#             else:
#                 print ("You guessed it!")
#                 print("The number I guessed was :", num)
#                 break
#         else:
#             print("Number should be in range of 0 and 100 (included)")

# __main__()


#################           SECOND PROJECT           #############
# import random

# ROCK = 'r'
# SCISSORS = 's'
# PAPER = 'p'

# choices_to_print = {
#     'r' : "Rock",
#     's' : "Scissors",
#     'p' : "Paper"
# }

# choices = tuple(choices_to_print.keys())


# def get_userchoice():
#      while True:
#         user_input = input('Your Choice : ').lower()
#         if user_input not in choices:
#             print("Choose from r/p/s\n")
#         else:
#             return user_input

    
# def determine_winner(user_input, computer):
    
#         if user_input == computer:
#             print("Tie!")
#         elif (
#             (user_input == SCISSORS and computer == PAPER) or 
#             (user_input == PAPER and computer == ROCK) or
#             (user_input == ROCK and computer == SCISSORS)):
#             print("You win!")
#         else:
#             print("Computer wins!")


# def __main__():
#     while True:
#         print("Rock, Paper, Scissors (r/p/s)?")
        
#         computer = random.choice(choices)

#         user_input = get_userchoice()
        
#         print("\n")
#         print(f'You Chose {choices_to_print[user_input]}')
#         print(f'Computer Chose {choices_to_print[computer]}')

#         determine_winner(user_input, computer)
        
#         choice = input("\nWant to play again? (y/n)").lower()
#         if choice == "y":
#             print("\n")
#             continue
#         else:
#             break

# __main__()
        
        
    

#################           THIRD   PROJECT           #############

# from datetime import datetime

# class DataStream:
#     def __init__(self, source_name, isactive):
#         self.source_name = source_name
#         self.isactive = isactive

#     def get_timetamo():
#         return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    

# class TextStream(DataStream):
#     def __init__(self, source_name, isactive):
#         super().__init__(source_name, isactive)
    
#     @staticmethod
#     def clean_payload(raw_text):
#         if (not raw_text.strip()):
#             text = "empty"
#             return text
#         else:
#             return raw_text.strip()
        

# message = "  \n ALIA IS THIS NAME OF THE GIRL  "
# data = TextStream("Alia", True)
# result = data.clean_payload(message)
# print(result)

# result = TextStream.clean_payload(" ")
# print(result)