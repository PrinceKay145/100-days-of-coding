from replit import clear
from art1 import logo
print (logo)

bid ={}
go_again = True
while go_again:
  name = input("What is your name: ")
  bid_price = int(input("What is your bid price: $"))
  bid[name] = bid_price
  try_again = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
  if try_again == "no":
    clear()
    go_again = False
  elif try_again=="yes":
    clear()
final_bid = 0
final_name = ""
for price in bid:
  if bid[price] > final_bid:
    final_bid = bid[price]
    final_name = price
print(f"The highest bid is {final_bid}, and {final_name} is the winner.")
print(bid)