# str_length = input ("Please enter length: \n")
# str_width = input ("Please enter width: \n")

# #Convert Type
# length = float (str_length)
# width = float (str_width)

# # Calculate length and width

# area = length*width
# str_area = str(area)  
# print ("The total area is : " + str_area)

str_length = input ("Enter your length : \n")
str_width = input ("Enter your width: \n")
str_price = input ("Enter your 1 meter: \n")

length =  float (str_length)
width = float (str_width)
price = float (str_price)
area = length * width
total_price = price * area
str_area = str (area)
str_price = str (total_price)

print ("your arrea is : \n" + str_area)
print ("Give the guy: \n $" + str_price)

 



