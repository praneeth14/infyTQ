# PF-Exer-26

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def find_strong_numbers(num_list):
    strong_num_list = []
    for num in num_list:
        if not num:
            continue
        sum = 0
        temp = num
        while (temp > 0):
            sum += factorial(temp % 10)
            temp //= 10
        if sum == num:
            strong_num_list.append(num)
    return strong_num_list


num_list = [145, 375, 100, 2, 10]
strong_num_list = find_strong_numbers(num_list)
print(strong_num_list)
