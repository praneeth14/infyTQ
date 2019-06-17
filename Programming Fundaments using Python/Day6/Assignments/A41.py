# PF-Assgn-41
def find_ten_substring(num_str):
    result_list=[]
    for i in range(0,len(num_str)):
        sum=int(num_str[i])
        for j in range(i+1,len(num_str)):
            sum=sum+int(num_str[j])
            if sum==10:
                result_list.append(num_str[i:j+1])
    return result_list

num_str = '3523014'
print("The number is:", num_str)
result_list = find_ten_substring(num_str)
print(result_list)
