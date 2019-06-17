#PF-Tryout
def find_armstrong(number):
    power=len(str(number))
    temp=number
    sum=0
    while(number>0):
        rem=number%10
        sum+=rem**power
        number//=10
    if(temp==sum):
        return True
    else:
        return False

number=371 #provide different numbers and check the output
if(find_armstrong(number)):
    print(number,"is an Armstrong number")
else:
    print(number,"is not an Armstrong number")