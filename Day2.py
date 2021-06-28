# We have a situation, where we need to use list and get details of students in every cities where we have ANSSIR
# so we can decide which city will host the next convention, judging from the man power.
import random
Moscow =[]
Petersburg = []
Krasnodar = []
Rostov =[]
Belgorod =[]
ANSSIR = [Moscow, Petersburg, Krasnodar, Belgorod, Rostov]
your_city = input("What city are you from? ")
your_name = input('What is your name? ')
name = your_name.upper()
city = your_city.lower()
if your_city == "moscow":
    Moscow.append(name)
print(ANSSIR)
#I don't know how to make use of the same code again, i would have love to continue to append
#Untill the user choose to end the cycle.

#working with random
#Creating a simple addition game
print("Welcome to my simple addition game.")
first_number = random.randint(0,100)
second_number = random.randint(0,100)
operation = input('''
Which operation would you like to do:
1 for + (addition)
2 for * (multiplication)
3 for / (division)
4 for - (subtraction)
0 to exit the game
\n''')
if operation == "1":
    print(f'What is the sum of {first_number} + {second_number}')
    answer = int(input("Answer here = "))
    if answer == first_number + second_number:
        print ("That is correct!")
    else:
        print("Ooops, you got that wrong...")
elif operation == "2":
    print(f'What is the multiplication of {first_number} * {second_number}')
    answer = int(input("Answer here = "))
    if answer == first_number * second_number:
        print("That is correct!")
    else:
        print("Ooops, you got that wrong...")

elif operation == '3':
    print(f'What is the division of {first_number} / {second_number}')
    answer = int(input("Answer here = "))
    if answer == first_number / second_number:
        print("That is correct!")
    else:
        print("Ooops, you got that wrong...")

elif operation == "4":
    print(f'What is the subtraction of {first_number} - {second_number}')
    answer = int(input("Answer here = "))
    if answer == first_number - second_number:
        print("That is correct!")
    else:
        print("Ooops, you got that wrong...")
elif operation == "0":
    exit()
else:
    print("Please try again, and pick between the given options. Thank you")