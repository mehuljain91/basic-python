import random

# function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

# generate random uppercase letter using ascii code
upperCaseLetter1 = chr(random.randint(65,90)) 
upperCaseLetter2 = chr(random.randint(65,90)) 

# generate random lowercase letter using ascii code
lowerCaseLetter1 = chr(random.randint(97, 122)) 
lowerCaseLetter2 = chr(random.randint(97, 122))

# generate random digit letter using ascii code
digit1 = chr(random.randint(48, 57))
digit2 = chr(random.randint(48, 57))

# generate random special letter using ascii code
specialChar1 = chr(random.randint(33, 47))
specialChar2 = chr(random.randint(33, 47))

#Generate password using all the characters, in random order
password = upperCaseLetter1 + upperCaseLetter2 + lowerCaseLetter1 + lowerCaseLetter2 + digit1 + digit2 + specialChar1 + specialChar2
password = shuffle(password)

#Ouput
print(password)
