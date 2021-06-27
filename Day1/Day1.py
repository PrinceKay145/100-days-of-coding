#Day1 - 100days of coding
#Writing a program that tell you about yourself, after series of questions.
print('Let us know more about you...\n')
surname = input('What is your surname? ')
firstName= input("What is your first name? ")
print('\n')
print(f'{firstName} born into the family of {surname}, I am glad to have you around today...\n')
print("Let's talk some steps forward together\n")
country = input('So, what country are you from? ')
print('\n')
print("----------------------------------------------------\n")
print(f"So, you mentioned that you live in {country}\n")
print('Are you a student?\n')
print("What do you do for a living? \n")
#if you are to live for 100years
print("----------------------------------------------------\n")
ag = input('So, how old are you? ')
age=100-int(ag)
months = int(age) * 12
days = int(age) * 365
weeks = int(age) * 52
print('\n')
print(f"Alright,let's assume you'll live a 100 years on earth,  as of this year, you have {days} days {weeks} weeks {months} months left.... \n")
print("Please ensure you make each day count...\n")
print("----------------------------------------------------\n")
print(f"So {firstName}, without taking much of your time. Have a nice day...\n")
print("It was nice having this little chat with you \n")
city=input("Which city do you actually stay? ")
print('\n')
print(f'I hope to see you around {city} someday, I will be visiting {country}, real soon...\n')
print("Bye for now...")