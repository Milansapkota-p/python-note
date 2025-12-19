import random
#randint is function which gernerate random integer value
target=random.randint(1,100)
while(1):
    userChoice=int(input("Guess the target:"))
    if(userChoice==target):
        print("congratulation your guess is correct")
        break
    elif(userChoice>target):
        print("Your number was big .Take a smaller guess")
    else:
        print("your number was small .Take a bigger guess")
print("-----Game over-----")