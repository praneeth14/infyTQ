# PF-Assgn-38

def check_double(number):
    double_number=number*2
    s_number=str(number)
    ds_number=str(double_number)
    if(len(s_number)!=len(ds_number)):
        return False
    for i in s_number:
        if i not in ds_number:
            return False
    return True


# Provide different values for number and test your program
print(check_double(125874))
