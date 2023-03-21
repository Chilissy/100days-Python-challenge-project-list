import clear

def add(n1, n2):
    return n1 + n2 

def subtract(n1, n2):
    return n1 - n2 

def multiply(n1, n2):
    return n1 * n2 

def divide(n1, n2):
    return n1 / n2 


operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply,
    "/": divide
}


def calculator():
    print("Welcome to calculator!")
    n1 = float(input("What number one: "))
    n2 = float(input("What number two: "))
    
    for key in operations:
        print(key)
        
    op_sym = input("What operation")
            
    calculation_function = operations[op_sym]
    first_answer = calculation_function(n1, n2)
    print(first_answer)
    i = float(first_answer)

    x = "y"
    
    while x == "y":
        for key in operations:
            print(key)
            
        op_sym = input("What operation")
        j = float(input("What number one: "))
        calculation_function = operations[op_sym]
        i = calculation_function(i, j)
        print(i)
        x = input("Continue? ")
    else:
        calculator()

calculator()
