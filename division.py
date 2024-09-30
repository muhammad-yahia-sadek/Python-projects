# Division
#print (1000 // 107)
# Floor Division // باقي القسمة
# print (341 % 60) # بيطلع باقي القسمة و بتاجهل الرقم الصحيح 
str_course = input ("Enter your hours : \n")
total_minutes = int (str_course)
hours = int (str_course) // 60 
miuntes = int (str_course) % 60
print (" your course in  " + str(hours) +" hours and " + str (miuntes) + " miuntes")

sum_hours = input ("Enter your secounds : \n")
total_hours = int (sum_hours)
hours = str (total_hours) * 120
miuntes = str (total_hours) * 60
secound = str (total_hours)
print ("your hours is " + str (hours) + " hours and " + str(miuntes) + " miuntes and " + str (secound) + "secounds")

# born_year =int ( input ("How old are you :\n") )
# year = 2024
# born_in = (year - born_year)
# print ("you are born in the year " + str (born_in))

born_year =int ( input ("How old are you :\n") )
#year = 2024
print (f"you are born in the year {2024 - born_year}") # {} curly brackets does not need to type (float , int , str)
