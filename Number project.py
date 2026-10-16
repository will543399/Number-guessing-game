
""" while True:
    z = input("Enter a number to multiply by 2 (or 'exit' to quit): ")
    if z == "exit":
        break
    number = float(z)
    print(number * 2)

while True:
    z = input("Enter a number to multiply by 5 (or 'exit' to quit): ")
    y=input("enter a number you want to multiply")
    if  z == "exit":
        break
    if y=='exit':
        break
    number = float(z)
    print(number * y) """

import random
mini=1
maxa=100
guess=0
rand=random.randint(mini,maxa)

history=[]
while True:
    y=input("guess a number from 1-100, Exit to leave")
    history.append(y)
    guess=guess+1
    if y =="exit":
        break
    elif int(y)> rand:
        print (f"You Guessed" + str(history))
        print(f"number of guesses"+str(guess))
        print("lower")
    elif int(y)<rand:
        print (f"You guessed"+ str(history))
        print(f"number of guesses "+ str(guess))
        print("higher")
    elif int(y)==rand:
        print(f"correct! it is", (rand))
        break;