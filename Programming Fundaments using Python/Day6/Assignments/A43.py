#PF-Assgn-43

def find_smallest_number(num):
    #start writing your code here
    n=1
    while(True):
        count=0
        for i in range(1,n+1):
            if(n%i==0):
                count+=1
        if(count==num):
            return n
        else:
            n+=1

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)