# PF-Assgn-34
def find_pairs_of_numbers(num_list, n):
    count = 0
    for i in range(0, len(num_list)):
        for j in range(i+1, len(num_list)):
            if (num_list[i] + num_list[j] == n):
                count += 1
    return count


num_list = [10,20,30,40,50]
n = 100
print(find_pairs_of_numbers(num_list, n))
