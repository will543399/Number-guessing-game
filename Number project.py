
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
    inty=int(y)
    if y=="exit":
        break
    elif inty> rand:
        print (f"You Guessed" + str(history))
        history.append(inty)
        guess==inty
        print("lower")
    elif inty<rand:
        print (f"You guessed"+ str(history))
        history.append(inty)
        guess==inty
        print("higher")
    elif guess==rand:
        print("correct")
        break

    
