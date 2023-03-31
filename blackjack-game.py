# ----- THE CODE BELOW WAS ENTIRELY WRITTEN BY ME. 
# ----- AS A PART OF A CHALLENGE, I HAD AN OPTION TO CHECK THE HINTS THAT COURSE MASTER PROVIDED WHICH I DID NOT USED.
# ----- IT TOOK ME AROUND 8 FULL HOURS TO COMPLETE THIS CHALLENGE

import random

cards = {11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10}

my_hand = 0
pc_hand = 0
n = 1
m = 1
sum = 0
dsum = 0
list_of_your_cards = []
list_of_dealer_cards = []
list_your_hand = []
list_dealer_hand = []


""" BELOW: Function, that append my hand by one random card."""
def uadd_card():
    list_your_hand.append(random.randint(2, len(cards) - 1))

""" BELOW: Function, that append dealers hand by one random card."""
def dadd_card():
    list_dealer_hand.append(random.randint(2, len(cards) - 1))

""" BELOW: Function, that check if there's an ace in my hand. If it is, it changes ace value from 11 to 1."""
def check_ace():
    for ace in range(0, len(list_your_hand)):
        if list_your_hand[ace] == 11:
            list_your_hand[ace] = 1

""" BELOW: Function, that check if there's an ace in dealers hand. If it is, it changes ace value from 11 to 1."""
def check_dace():
    for ace in range(0, len(list_dealer_hand) - 1):
        if list_dealer_hand[ace] == 11:
            list_dealer_hand[ace] = 1
        else:
            return False

""" BELOW: Function that sum card on my hand."""
def my_sum(sum):
    for card in range(0, len(list_your_hand)):
        x = list_your_hand[card]
        sum = sum + x
    return sum

""" BELOW: Function that sum card on dealers hand."""
def d_sum(dsum):
    for card in range(0, len(list_dealer_hand)):
        x = list_dealer_hand[card]
        dsum = dsum + x
    return dsum

""" BELOW: Everyone gets 2 cards at the beginning."""
uadd_card()
uadd_card()
dadd_card()
dadd_card()

""" BELOW: Checks if 2 aces in hand and if I or dealer got Blackjack."""
if my_sum(sum) > 21:
    check_ace()
if d_sum(dsum) > 21:
    check_dace()
if my_sum(sum) == 21 and d_sum(dsum) == 21:
    print("Draw!")
if my_sum(sum) == 21:
    print("You won!")
if d_sum(dsum) == 21:
    print("You lost!")

print(f"Yours = {list_your_hand} sum: {my_sum(sum)}")
print(f"Dealers = [x, {list_dealer_hand[1]}]")

""" BELOW: If nobody got Blackjack before, system asks user if to add a new card or pass. If 'HIT' then it checks if the sum is higher than 21, and if there's any
        ace, that could change the sum value. If the user sum is above 21, it prints 'lost'. If 'STAND', then system does the same for dealer. Then compares."""
while input("Hit or stand?") == 'h':
    uadd_card()
    if my_sum(sum) > 21:
        check_ace()
        if my_sum(sum) > 21:
            print(f"Yours = {list_your_hand} sum: {my_sum(sum)}")
            print(f"Dealers = {list_dealer_hand} sum: {d_sum(dsum)}")
            print("You lost!")
            quit()
    print(f"Yours = {list_your_hand} sum: {my_sum(sum)}")
else:
    print(f"Dealers = {list_dealer_hand} sum: {d_sum(dsum)}")
    while d_sum(dsum) <= 16:
        dadd_card()
        if d_sum(dsum) > 21:
            print(f"Yours = {list_your_hand} sum: {my_sum(sum)}")
            print(f"Dealers = {list_dealer_hand} sum: {d_sum(dsum)}")
            print("You won!")
            quit()
        print(f"Yours = {list_your_hand} sum: {my_sum(sum)}")
        print(f"Dealers = {list_dealer_hand} sum: {d_sum(dsum)}")
    if my_sum(sum) > d_sum(dsum):
        print("you won")
        quit()
    elif my_sum(sum) == d_sum(dsum):
        print("draw")
        quit()
    else:
        print("you lost")
        quit()

        # ---------------------------------------------------------------------- previous
        # versions
        # below

# if input1 == 'h':
#     uadd_card()
#     if my_sum(sum) > 21:
#         check_ace()
#     print(f"Yours = {list_your_hand} sum: {my_sum(sum)}")
# else:
#     while d_sum(dsum) <= 16:
#         dadd_card()
#         check_dace()
#         print(f"Yours = {list_your_hand} sum: {my_sum(sum)}")
#         print(f"Dealers = {list_dealer_hand} sum: {d_sum(dsum)}")
#     if my_sum(sum) > d_sum(dsum):
#         print("you won")
#         quit()
#     elif my_sum(sum) == d_sum(dsum):
#         print("draw")
#         quit()
#     else:
#         print("you lost")
#         quit()

# input2 = input("Hit or stand?")
# if input2 == 'h':
#     uadd_card()
#     if my_sum(sum) > 21:
#         check_ace()
#     print(f"Yours = {list_your_hand} sum: {my_sum(sum)}")
# else:
#     while d_sum(dsum) <= 16:
#         dadd_card()
#         check_dace()
#         print(f"Yours = {list_your_hand} sum: {my_sum(sum)}")
#         print(f"Dealers = {list_dealer_hand} sum: {d_sum(dsum)}")
#     if my_sum(sum) > d_sum(dsum):
#         print("you won")
#         quit()
#     elif my_sum(sum) == d_sum(dsum):
#         print("draw")
#         quit()
#     else:
#         print("you lost")
#         quit()

# input3 = input("Hit or stand?")
# if input3 == 'h':
#     uadd_card()
#     check_ace()
#     print(f"Yours = {list_your_hand} sum: {my_sum(sum)}")
# else:
#     while d_sum(dsum) <= 16:
#         dadd_card()
#         check_dace()
#         print(f"Dealers = {list_dealer_hand} sum: {d_sum(dsum)}")
#     if my_sum(sum) > d_sum(dsum):
#         print("you won")
#         quit()
#     elif my_sum(sum) == d_sum(dsum):
#         print("draw")
#         quit()
#     else:
#         print("you lost")
#         quit()

# input4 = input("Hit or stand?")
# if input4 == 'h':
#     uadd_card()
#     check_ace()
#     print(f"Yours = {list_your_hand} sum: {my_sum(sum)}")
# else:
#     while d_sum(dsum) <= 16:
#         dadd_card()
#         check_dace()
#         print(f"Dealers = {list_dealer_hand} sum: {d_sum(dsum)}")
#     if my_sum(sum) > d_sum(dsum):
#         print("you won")
#         quit()
#     elif my_sum(sum) == d_sum(dsum):
#         print("draw")
#         quit()
#     else:
#         print("you lost")
#         quit()

# input5 = input("Hit or stand?")
# if input5 == 'h':
#     uadd_card()
#     check_ace()
#     print(f"Yours = {list_your_hand} sum: {my_sum(sum)}")
# else:
#     while d_sum(dsum) <= 16:
#         dadd_card()
#         check_dace()
#         print(f"Dealers = {list_dealer_hand} sum: {d_sum(dsum)}")
#     if my_sum(sum) > d_sum(dsum):
#         print("you won")
#         quit()
#     elif my_sum(sum) == d_sum(dsum):
#         print("draw")
#         quit()
#     else:
#         print("you lost")
#         quit()

# input6 = input("Hit or stand?")
# if input6 == 'h':
#     uadd_card()
#     check_ace()
#     print(f"Yours = {list_your_hand} sum: {my_sum(sum)}")
# else:
#     while d_sum(dsum) <= 16:
#         dadd_card()
#         check_dace()
#         print(f"Dealers = {list_dealer_hand} sum: {d_sum(dsum)}")
#     if my_sum(sum) > d_sum(dsum):
#         print("you won")
#         quit()
#     elif my_sum(sum) == d_sum(dsum):
#         print("draw")
#         quit()
#     else:
#         print("you lost")
#         quit()
