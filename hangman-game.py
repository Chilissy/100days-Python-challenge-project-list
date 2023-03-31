#Password Generator Project
import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Hej, zagrajmy w wisielca po angielsku!")

word = "mammamia"
point = 0
position = 0
wordlist = list(word)     # Creating the list for the word
mistake = 5
under = "_"
hiddenword = ""

spaces = list(word)
x=0

for letter in word:
  hiddenword += under

hiddenlist = list(hiddenword) # Creating new list for the underscores

print(hiddenword)

print(f"Dzisiejsze hasło ma {len(wordlist)} liter")


i = len(word)
u = ""


while hiddenlist != wordlist:
  
  your_letter = input("\nWybierz literkę: ")

  it_was = False
  
""" BELOW: While loop goes on, until the user finds out the word. First user input a letter. Then it check if the letter 'was' already in the word. """
  for x in range(0, len(hiddenlist)):
    if hiddenlist[x] == your_letter:
      print("Ta litera już była")
      it_was = True
      break
                   
""" BELOW: This code checks, if the letter the user had input is correct. If no, while loop continues asking for another letter. If yes, the letter use 
    'for' loop to see where the letter is, check the list, and changes correspondent underscores into letter."""
  x = 0
  slowo = ""
  for letter in wordlist:
    if letter == your_letter:
      hiddenlist[x] = your_letter
      x += 1
        
    elif letter == "_":
      hiddenlist[x] = "_"
      
    elif letter != your_letter:
      x += 1
      
      
  x = 0
  for x in range(0, len(word)):
    slowo += hiddenlist[x]
  
  x = 0
  for letter in wordlist:
    if letter != your_letter:
      x += 1
      
""" BELOW: Checks your life score. If it goes to 0, user lose."""
  if x >= i:
    mistake -= 1
    print("Sprobuj ponownie")
    print(f"{mistake} lifes left")
  
  print(slowo)

  count1 = len(word) - 1

""" BELOW: Counters correctly guessed places. If user guesses all the hidden letter before losing his life score, he wins."""
  for letter in wordlist:
    if your_letter == letter and it_was == False:
      point += 1
      count1 -= 1
  print(f"Posiadasz {point} z {len(wordlist)} punktów!")

  if point == len(wordlist):
    print("WYGRAŁEŚ")
    
    
  if mistake == 0:
    print("Przegrałeś")
    
