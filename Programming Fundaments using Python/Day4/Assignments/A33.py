# PF-Assgn-33

def find_common_characters(msg1, msg2):
    msg1=''.join(msg1.split())
    msg2=''.join(msg2.split())
    common_characters=[]
    for i in msg1:
        if i in msg2:
            if i not in common_characters:
                common_characters.append(i)
    if(not len(common_characters)):
        return -1
    return ''.join(common_characters)

# Provide different values for msg1,msg2 and test your program
msg1 = "I like Python"
msg2 = "Java is a very popular language"
common_characters = find_common_characters(msg1, msg2)
print(common_characters)
