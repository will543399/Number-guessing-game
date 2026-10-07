
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
rand=random.randiant(mini,maxa)
y=input("guess a number from 1-100")

while True:
    if y=="exit":
        break
    elif y>rand:
        print (f"You Guessed" guess_history)
        guess_history=y+guess_history
        print("lower")
    elif y<rand:
        print (f"You guessed"guess_history)
        guess_history=y+guess_history
        print("higher")
    elif y==rand:
        print("correct")

    
