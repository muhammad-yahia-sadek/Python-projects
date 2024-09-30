area = str(input("Please enter your area :(Cairo), (Alexandria) , (Tanta) \n"))
if area.lower() == ("cairo"):
    print ("you choose cairo")
elif area.upper() == ("ALEXANDRIA"):
    print("you choose alexandria")
elif area.lower() == ("tanta"):
    print ("you choose Tanta")
else:
    print ("Your area does not exiting try again")


# location = str(input("PLease Choose your location : (Ryhiad), (Abha), (Dammam)\n"))
# if location.lower() == "ryhiad":
#     print("you Choose Ryhiad , welcome")
# elif location.upper() == "ABHA":
#     print("you Choose Abha , welcome")
# elif location.upper() == "dammam":
#     print("you Choose Dammam , welcome")
# else:
#     print("Sorry this location not here")

country = str(input("Enter your Country : (Ksa) , (Egypt) , (Other)\n"))
if country.lower() == "ksa" or country.lower() == "egypt" or country.lower() == "Other":
    print("You Choose Country {country}")
else:
    print("You not choose the right country")

age = int(input("Please type your age \n"))
license = input("Are you have a license\n")
if age >= 18 and license.lower == "yes":
    print("you can drive")
elif age < 18 and license.lower() == "no":
    print ("Sorry you can not drive")
else:
    print ("Sorry you can connect to Traffic station")