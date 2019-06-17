#PF-Assgn-44

def find_duplicates(list_of_numbers):
    #start writing your code here
    duplicate_list=[]
    for num in list_of_numbers:
        if(list_of_numbers.count(num)>1):
            if num not in duplicate_list:
                duplicate_list.append(num)
    return duplicate_list

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)