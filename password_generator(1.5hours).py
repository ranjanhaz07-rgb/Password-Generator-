# To generate password with only letters and digits

# import random
# import string

# letters = string.ascii_letters
# digits = string.digits

# all_char = letters + digits

# length = int(input("Enter your password length:"))

# password = ""

# for i in range(length):
#     password += random.choice(all_char)

# print("Generating Password.....")
# print("Generated Password:", password)

# To generate passwords with letters, digits and punctuations

import random
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_char = letters + digits + symbols

while True:
  count_letters = 0
  count_digits = 0
  count_symbols = 0
  try:
     length = int(input("Enter your password length:"))
  except ValueError:
     print("Enter numbers only!") 
     continue
  
  if length <= 1:
      print("Length must be greater than 0")
      continue
     
  password = ""
  
  for i in range(length):
      password += random.choice(all_char)
  
  for ch in password:
     if ch in letters:
       count_letters += 1
     
     elif ch in digits:
        count_digits += 1
      
     elif ch in symbols:
        count_symbols += 1
  
  print("\nGenerating Password.....")
  print("Generated Password:-", password)
  
  if length >= 8 and count_letters >= 2 and count_digits >= 1 and count_symbols >= 2:
     print("Very Good Password!")
  
  elif length >= 6 and count_letters >= 1 and count_digits >= 1 and count_symbols >= 1:
     print("Good Password!")
  
  elif  length >= 8 and count_letters >=1 and count_symbols >= 1:
     print("Mid Password!")
  
  else:
     print("Bad Password!")
  
  choice = input("\nDo you want to regenerate the password? (Yes/No)").lower()
  if choice == "no":
     print("Program Ended!")
     break                 
