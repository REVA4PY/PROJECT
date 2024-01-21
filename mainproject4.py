#Random Password Generator using Python

#import the necessary modules
import string
import random

#input the length of password
length = int (input("Enter the length of password:"))

#Define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

#combine the data
all = lower + upper + numbers + symbols

#use random to create password
password = "".join(random.sample(all, length))

#To print the password
print("The Generated Password is:",password)




