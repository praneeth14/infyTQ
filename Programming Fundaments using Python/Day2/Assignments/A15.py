# PF-Assgn-15

def find_product(num1, num2, num3):
    product = 0
    # write your logic here
    if (num1 == 7):
        product = num2 * num3
    elif (num2 == 7):
        product = num3
    elif (num3 == 7):
        product = -1
    else:
        product = num1 * num2 * num3
    return product


# Provide different values for num1, num2, num3 and test your program
product = find_product(7, 6, 2)
print(product)
