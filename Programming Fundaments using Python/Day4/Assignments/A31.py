# PF-Assgn-31
def check_palindrome(word):
    i=0
    j=len(word)-1
    while(i!=j):
        if(word[i]==word[j]):
            i+=1
            j-=1
        else:
            return False
    return True


status = check_palindrome("malayalam")
if (status):
    print("word is palindrome")
else:
    print("word is not palindrome")
