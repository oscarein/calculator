import math

def plus (x, y):
    print("Svaret är",x+y)

def minus (x, y):
    print("Svaret är",x-y)

def delat (x, y):
    print("Svaret är",x/y)

def gånger (x, y):
    print ("Svaret är",x*y)

def roten (x):
    print("Svaret är", math.sqrt(x))

while True:

    print("Vilket räknesätt vill du använda?")

    print("1. Addition")
    print("2. Subtraktion")
    print("3. Divition")
    print("4. Multiplikation")
    print("5. Roten ur")

    val = int(input("Skriv in önskat räknesätt (1-5): "))
    
    if val == 5:
        n0 =  int(input("Skriv ett nummer: "))
    else:              
        n1 = int(input("Skriv ett nummer: "))
        n2 = int(input("Skriv in ett till nummer: "))


    if val == 1:
        plus(n1, n2)
    elif val == 2:
        minus(n1, n2)
    elif val == 3:
        delat(n1, n2)
    elif val == 4:
        gånger(n1, n2)
    elif val == 5:
        roten(n0)
