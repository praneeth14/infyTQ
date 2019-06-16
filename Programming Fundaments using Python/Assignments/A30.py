# PF-Assgn-30
def encode(message):
    encoded_list = []
    count = 1
    if(len(message)==1):
        return "1"+message
    for i in range (1, len(message)):
        if (message[i] == message[i - 1]):
            count += 1
        else:
            encoded_list.append(str(count))
            encoded_list.append(message[i - 1])
            count = 1
        if(i==len(message)-1):
            encoded_list.append(str(count))
            encoded_list.append(message[i])
    return ''.join(encoded_list)
# Provide different values for message and test your program
encoded_message = encode("ABBBBCCCCCCCCAB")
print(encoded_message)
