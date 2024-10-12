import random
my_env = random.random() * 5
print (f"my env is : {my_env}")

print ("""Welcome to the Coin Guessing Game!
       
          Choose a method to toss the coin
          1. Using random.rand.int()
          2. Using random.random()
""")
import random
choice_method = int (input ("Enter your Choice (1 or 2)\n"))
if choice_method == 1 :
    random_float=random.random()
    if random_float >= 0.5 :
        computer_result= "Heads"
    else :
        computer_result= "Tails"
elif choice_method == 2:
    random_int = random.randint(0,1)
    if random_int == 0 :
        computer_result= "Heads"
    else :
        computer_result= "Tails"
else :
    print("Please this is not correct choice")


user_choise = str(input("Please enter your choice (Heads or Tails): \n" ))
if user_choise.lower() == computer_result.lower() :
    print("Congrats you win")
else:
    print ("You are lose")
 
if choice_method == 1 or choice_method == 2:
     print(f"The coin toss result is: {computer_result}")

