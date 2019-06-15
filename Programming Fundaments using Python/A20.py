# PF-Assgn-20

def calculate_loan(account_number, salary, account_balance, loan_type, loan_amount_expected, customer_emi_expected):
    eligible_loan_amount = 0
    bank_emi_expected = 0

    # Start writing your code here
    # Populate the variables: eligible_loan_amount and bank_emi_expected
    loans={
        "Car":{
            "salary": 25000,
            "elm":500000,
            "emi":36
        },
        "House":{
            "salary": 50000,
            "elm": 6000000,
            "emi": 60
        },
        "Business": {
            "salary": 75000,
            "elm": 7500000,
            "emi": 84
        }
    }
    if(len(str(account_number))!=4 or not (str(account_number).startswith("1"))):
        print("Invalid account number")
        return
    if(account_balance<100000):
        print("Insufficient account balance")
        return
    if(loan_type not in loans.keys()):
        print("Invalid loan type or salary")
        return

    if(loans[loan_type]["salary"]>=salary):
        print("Invalid loan type or salary")
        return
    eligible_loan_amount=loans[loan_type]["elm"]
    bank_emi_expected=loans[loan_type]['emi']

    if(loan_amount_expected>eligible_loan_amount or customer_emi_expected>bank_emi_expected):
        print("The customer is not eligible for the loan")
        return
    else:
        print("Account number:", account_number)
        print("The customer can avail the amount of Rs.", eligible_loan_amount)
        print("Eligible EMIs :", bank_emi_expected)
        print("Requested loan amount:", loan_amount_expected)
        print("Requested EMI's:", customer_emi_expected)

    # Use the below given print statements to display the output, in case of success


    # Use the below given print statements to display the output, in case of invalid data.

    # Also, do not modify the above print statements for verification to work


# Test your code for different values and observe the results
calculate_loan(1001, 40000, 250000, "Car", 300000, 30)