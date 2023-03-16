# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

t1 = []
t2 = []
x = ""
y = 0
z = 0
q = 0
result = ""

for nr_letters in range(0, nr_letters):
    x = random.randint(0, len(letters) - 1)
    y = x
    y = t2.append(y)
    x = letters[x]
    result = result + x
    x = t1.append(x)

# --- cleaner ---

# list = []
# z1 = 0
# z2 = ""
#
# for nr_letters in range(0, nr_letters:
#     z1 = (random.randint(0, len(letters) - 1))
#     list.append(letters[z1])
#     z2 += letters[z1]
#     print(z2)


for nr_symbols in range(0, nr_symbols):
    x = random.randint(0, len(symbols) - 1)
    z = x
    z = t2.append(z)
    x = symbols[x]
    result = result + x
    x = t1.append(x)

for nr_numbers in range(0, nr_numbers):
    x = random.randint(0, len(numbers) - 1)
    q = x
    q = t2.append(q)
    x = numbers[x]
    result = result + x
    x = t1.append(x)

print(result)

rand = random.sample(range(len(t2)), len(t2))
x = 0

for i in range(0, len(rand)):
    # print(rand[x])
    y = rand[x]
    print(t1[y], end="")
    x += 1
