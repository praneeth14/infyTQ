# PF-Assgn-28
def find_max(num1, num2):
    max_num = -1
    # Write your logic here
    if (not num1 < num2):
        return max_num

    for num in range(num1, num2 + 1):
        if (num % 3 == 0 and num % 5 == 0 and len(str(num)) == 2):
            if (num > max_num):
                max_num = num

    return max_num


# Provide different values for num1 and num2 and test your program.
max_num = find_max(10, 15)
print(max_num)
