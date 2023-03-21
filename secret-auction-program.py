from replit import clear
#HINT: You can call clear() to clear the output in the console.

dict={}


def bidding():
    name = input("Name: ")
    bid = input("Bid: $")
    dict[bid] = name
    clear()

bidding()
bidding()

y = input("More bidders?: ")
while y == "yes":
    bidding()
    y = input("More bidders?: ")


m = 0

for key in dict:
    list_key = key
    x = int(key)
    if x > m:
        m = x

print(f"The winner is: " + dict['150'] + "!!!" + f" with the amount of: ${m}")



