def deposit(amount):
    global balance
    balance += amount
    

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
    else:
        print("Not enough balance")
    


balance = 0 
newTransaction = True

while newTransaction == True:
    data = input("Please enter the transaction details : ")
    data = data.lower()


    if data.startswith('d'):
        amount = int(data[2:])
        deposit(amount)
        print(f"{amount} has been deposited to your account")


    elif data.startswith('w'):
        amount = int(data[2:])
        withdraw(amount)
        print(f"{amount} has been debited from your account")


    k = input("Do you want to make another transaction :(y,n) ")
    if k == "y":
        pass
    elif k == 'n':
        newTransaction = False

print(f"Your balance is {balance}")
    
    





    
