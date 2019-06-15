# PF-Assgn-16
def make_amount(rupees_to_make, no_of_five, no_of_one):
    five_needed = 0
    one_needed = 0

    # Start writing your code here
    # Populate the variables: five_needed and one_needed
    req_five = rupees_to_make // 5
    req_one = rupees_to_make % 5
    if (req_five <= no_of_five):
        five_needed = req_five
    else:
        five_needed = no_of_five
        req_one = rupees_to_make - (five_needed * 5)
    if (req_one == 0):
        req_one = rupees_to_make - (five_needed * 5)
    if (req_one <= no_of_one):
        one_needed = req_one
    else:
        one_needed = no_of_one
    if ((five_needed * 5 + one_needed) == rupees_to_make):
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)


# Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(16, 1, 15)
