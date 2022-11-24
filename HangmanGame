#Password Generator Project
import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Siemanko, zagrajmy w wisielca po angielsku!")

word = "mammamia"
point = 0
position = 0
wordlist = list(word)
mistake = 5
under = "_"
hiddenword = ""

spaces = list(word)
x=0

for letter in word:
  hiddenword += under

hiddenlist = list(hiddenword)

print(hiddenword)

print(f"Dzisiejsze hasło ma {len(wordlist)} liter")


i = len(word)
u = ""

while hiddenlist != wordlist:
  
  your_letter = input("\nWybierz literkę: ")

  it_was = False
  
  for x in range(0, len(hiddenlist)):
    if hiddenlist[x] == your_letter:
      print("Ta litera już była")
      it_was = True
      break
                   
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
  if x >= i:
    mistake -= 1
    print("Sprobuj ponownie")
    print(f"{mistake} lifes left")
  
  print(slowo)

  count1 = len(word) - 1
  
  for letter in wordlist:
    if your_letter == letter and it_was == False:
      point += 1
      count1 -= 1
  print(f"Posiadasz {point} z {len(wordlist)} punktów!")

  if point == len(wordlist):
    print("WYGRALES")
    
    
  if mistake == 0:
    print("sorki, przegrałeś")
    
