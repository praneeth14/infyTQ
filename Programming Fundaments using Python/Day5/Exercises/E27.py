# PF-Tryout
def withdraw(account_list, balance_list, amount, account_number):
    for index in range(0, len(account_list)):
        if (account_list[index] == account_number):
            flag = True
            value = index
    if (flag == True):
        balance = balance_list[value]
        new_balance = balance - amount
        if (new_balance >= 500):
            balance_list[value] = new_balance
            print("Transaction completed successfully")
            print("Balance Amount :", new_balance)
        else:
            print("Insufficient Balance")
    else:
        print("Invalid Account number")


def deposit(account_list, balance_list, amount, account_number):
    for index in range(0, len(account_list)):
        if (account_list[index] == account_number):
            flag = True
            value = index
    if (flag == True):
        balance = balance_list[value]
        new_balance = balance + amount
        balance_list[value] = new_balance
        print("Transaction completed successfully")
        print("Balance Amount :", new_balance)
    else:
        print("Invalid Account number")


def balance_enquiry(account_list, balance_list, account_number):
    for index in range(0, len(account_list)):
        if (account_list[index] == account_number):
            flag = True
            value = index
    if (flag == True):
        balance = balance_list[value]
        print(balance)
    else:
        print("Invalid Account number")


account_list = [1001, 1002, 1003, 1004, 1005]
balance_list = [2500, 10000, 7000, 1500, 500]
amount = 1000
account_number = 1003
transaction_type = "Withdraw"

flag = None
if (transaction_type == "Withdraw"):
    withdraw(account_list, balance_list, amount, account_number)

elif (transaction_type == "Deposit"):
    deposit(account_list, balance_list, amount, account_number)

elif (transaction_type == "Balance Enquiry"):
    balance_enquiry(account_list, balance_list, account_number)

else:
    print("Invalid Transaction Type")
