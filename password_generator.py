# Generating random password
# User input the length of the password, then this app generate a string randomly

import random
import string

characters_lib = string.digits + string.ascii_letters + string.punctuation
while True:
    pass_length = input("Enter password's length: ")
    try:
        pass_length = int(pass_length)
        break
    except:
        print("Must be an integer, try again")
        continue

password = "".join(random.sample(characters_lib, pass_length))
print("Your password is: " + password)
