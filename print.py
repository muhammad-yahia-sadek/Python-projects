print ("""


██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║
██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝
       
 """)

print ("""
      ▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒
      ▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒
      ▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒
      ▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒
      ▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒

        """)
print ("Welcome to my island")
print("There are two doors in front of you. 🚪 a red door and 🚪  a blue door")
door = input("Which door do you want to open ?\n").lower()
if door == "red":
   print("Greate! now you entred a room")
   print("you found three boxes : 🎁 white, 🎁 black , 🎁 green")
   box = input("Which box do you open ?\n").lower()
   if box == "white" :
    print("Oops! you choose the snakes")
   elif box == "green" :
    print("Congratulation! you found the treasure!🪙🪙")
   elif box == "black":
    print ("Oops! you choose the spiders 🕷️🕷️🕷️ ")
   else: 
    print("Invalid Choice! 🤷🏽🤷🏽🤷🏽 ")

elif door == "blue" :
 print ("you choose the crocodile door")
 print  (" 🐊🐊🐊🐊 Game Over")
else: 
   print("Invalid Choice! 🤷🏽🤷🏽🤷🏽 ")
