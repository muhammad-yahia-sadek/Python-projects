is_egyption = input("Are you Egyption : Type 'yes' , 'No' \n").lower()
if is_egyption == "yes":
    print("Good , this is the frist step")
    is_18 = input("Are you older than or 18 : Type 'Yes' ,'No'\n").lower()
    if is_18 == "yes":
      print("You can get the Egyption ID")
    else:
      print("Sorry you should 18 to get ID")

else:
   print("this service for Egyption")


is_adult= input("Are you adult? Type : 'Yes' or 'No'\n").lower()
if is_adult == "yes":
   print("Good , you can Access your Data ")
   is_ID_egy = input("Do you have an ID? Type : 'Yes' or 'No'").lower()
   if is_ID_egy == "yes":
      print("You Can Have a passport")
   else:
      print("Sorry should be have an ID to get passport")
else:
   print("Sorry this service for egyption")


box = input("Which box do you open ?\n").lower
if box == "white" :
   print("Oops! you choose the snakes")
elif box == "green" :
   print("Congratulation! you found the treasure!🪙🪙")
elif box == "black":
   print ("Oops! you choose the spiders 🕷️🕷️🕷️ ")
else: 
   print("Invalid Choice! 🤷🏽🤷🏽🤷🏽 ")