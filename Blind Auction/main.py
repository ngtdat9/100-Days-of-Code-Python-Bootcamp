from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the blind auction")
bidders = {}
while True:
  name = input("What is your name\n")
  bid = input("How much do you want to bid?\n$")
  bidders[name] = bid
  more = input("Is there any other who want to place a bid? yes or no?\n")
  if more == 'yes':
    clear()
  elif more == 'no':
    break
highestbid = 0
for name in bidders:
  bidders[name] = int(bidders[name])
  if bidders[name] > highestbid:
    highestbid = bidders[name]
for name in bidders:
  bidders[name] = int(bidders[name])
  if bidders[name] == highestbid:
    print(f"The winner is {name} with the bid of {bidders[name]}")