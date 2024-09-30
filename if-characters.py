number_of_chair = float (input("Enter the number of chair\n"))
if number_of_chair != 13:  #not equal
 print("you win")
else:
  print("sorry you are not win")

Password = str (input("Enter your password\n"))
if Password == ("abc"):
  print("you password write")
else:
  print ("your password wrong")

welcome = str(input("Welcome to the app \n"))
if welcome == ("yes"):
  print("you write yes")
elif welcome == ("no"):
  print("you write no")
elif welcome == ("maybe"):
  print("you write maybe")
else:
  print("waring you need to listen the rules")


guess = float(input("Guess the number \n"))
if guess == 8:
  print("you are write congrate")
else:
  print ("hahahahaha Wrong")