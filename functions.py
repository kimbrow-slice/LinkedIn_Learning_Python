# def is short for define similar to JS's function
#parameters and arguments
credintals = True

def login_user():
#Auth Login Fail
    if(credintals != True):
        print("---------------------")
        print("Sorry Username or Password is incorrect! ")
        print("Try Again!")
        print("---------------------")
        

#Auth login Success
    else :
        print("---------------------")
        print("Your account has been successfully authenticated! ")
        print("---------------------")
        print("Welcome Back Jeffery!")
        

login_user()


print("---------------------")

def website_user(Admin):
    if(Admin == 1):
        print("Checking the balance now!")
    
    if(Admin == 0):

        print("Oh No! Looks like we can't find your account!")

website_user(1)



print("---------------------")
# function to return a value

def withdraw_money(current_balance, amount):
    if(current_balance >= amount):
        current_balance = current_balance- amount
        return current_balance
    
balance = withdraw_money(1400, 750) 

if(balance <= 100):
    print("You need to make a deposit")
else:
    print("No need to make a deposite today!  $",balance )
