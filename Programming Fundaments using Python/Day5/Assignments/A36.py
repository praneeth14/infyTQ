# PF-Assgn-36
def create_largest_number(number_list):
    largest_number=''
    number_list.sort(reverse=True)
    for num in number_list:
        largest_number+=str(num)
    return int(largest_number)

number_list = [23, 45, 67]
largest_number = create_largest_number(number_list)
print(largest_number)
