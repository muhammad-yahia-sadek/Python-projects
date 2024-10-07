import random
my_random = random.randint(0,10)
print(my_random)

import random 
check_number = random.randint(1000,9999)
secret_number = int (input("Enter your secret number\n"))

if len(str(secret_number)) != 4 :
    print ("please enter 4 digits")
elif secret_number == check_number :
    print ("success it is match pin_code")
else:
    print("try one more time")
    print (f"the computer generate the random pin_code is : {check_number}")