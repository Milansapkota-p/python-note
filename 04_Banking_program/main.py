#Building the logic of simple Banking system using function
def show_balance():
    print(f"your balance is Rs {balance}")
def deposite():
    amount=(input("Enter amount you want to deposite:"))
    if not amount.isdigit():
        print("Please enter amount in number")
    elif int(amount)<=0:
        print("Please enter higher amount than zero")
    else:
        print(f"Rs{amount} is successfully deposited")
        return balance+int(amount)        
def withdraw():
    amount=(input("Enter amount you want to withdraw:"))
    if not amount.isdigit():
        print("Please enter amount in number")
    elif int(amount)>balance:
        print("Insufficient balance")
    else:
        print(f"Rs{amount} is successfully Withdrawn")
        return balance-int(amount)

balance=0
running=True
while running:
    print("welcome to our Milan bank")
    print("1.Check balance")
    print("2.Deposite")
    print("3.Withdraw")
    print("4.Exist")
    user_input=input("Enter your choice:")
    if user_input=='1':
        show_balance()
    elif user_input=='2':
        balance=deposite()
    elif user_input=='3':
        balance=withdraw()
    elif user_input=='4':
        running=False
    else:
        print("Invlide choice")
print("Thank you for visit your site")