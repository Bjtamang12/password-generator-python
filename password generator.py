#importing random module
import random


#Length of password
LENGTH = 12

DIGITS = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] #if digits are in integer then it can't be aadded to string
SYMBOLS =[ '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
UPPER_letters = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#Combining all letters
combined_words = DIGITS + SYMBOLS + UPPER_letters + lower_letters


#Taking a random word from each
rand_digits = random.choice(DIGITS)
rand_symbols = random.choice(SYMBOLS)
rand_upper = random.choice(UPPER_letters)
rand_lower = random.choice(lower_letters)


#Storing the 4 random word
temp_password = rand_digits + rand_symbols + rand_upper + rand_lower


#Using for loop to create a password having length 12
for index in range(LENGTH - 4):
    temp_password += random.choice(combined_words)
    
  
#Converting temp_password into list to shuffle it  
list_pass = list(temp_password)
random.shuffle(list_pass)


# Converting the list again into a string to form the final password
password = ''.join(list_pass)
print(password)