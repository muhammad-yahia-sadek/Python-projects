# colors = []
# colors.append("red")
# print (colors)

color = []
choice = input  ("Add the first color you like : \n")
color.append(choice)
new_color = input  ("Do you want to add more colors ? : Yes or No \n ").lower()

if new_color == "yes":
    choice = input  ("Add the first color you like : \n")
    color.append(choice)
    print ("The colors you like are : \n")
    print(color)
else:
    print ("your favorite color is :")
    print(color)