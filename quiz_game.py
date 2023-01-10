print("Welcome to computer Quiz")\

playing = input("do you wanna play? ")

if playing != "yes":
    quit()

print("Okay let's play the game :) ")

answer = input("What does CPU stands for? ")
if answer == ("central processing unit"):
    print("correct!")
else:
    print("incorrect!! :(")
    
answer = input("What does GPU stands for? ")
if answer == ("graphic processing unit"):
    print("correct!")
else:
    print("incorrect!! :(")