##A Loop and A random password generator
import random
#First Project
#A game where any number divisble by 7 is changed to "Bottles"
#and any number that has 7 in it is also changed to "Bottles"
# for i in range (1, 101):
#     if i%7==0:
#         print("Bottles")
#     else:
#         print(i)

##Second Project
#generating a password from List of Letters(both upper and lower case), numbers and symbols

#to do this i have to manually create lists of numbers, letters and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#and then take the user's choice of what length they want
len_letters=int(input("How many letters do you want in your password? "))
len_numbers=int(input("How many numbers do you want in your password? "))
len_symbols=int(input("How many symbols do you want in your password? "))

#now the generation of the password
#i will create a list to save the random password
password_list = []
for i in range(1, len_letters+1):
    password_list += random.choice(letters)
for i in range(1, len_numbers+1):
    password_list += random.choice(numbers)
for i in range(1, len_symbols+1):
    password_list += random.choice(symbols)

random.shuffle(password_list)
#Now it is time to take it out of the list with the for loop
password=""
for i in password_list:
    password += i
print(password)