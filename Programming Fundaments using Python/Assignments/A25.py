# PF-Tryout

# debug the below code
counter1 = 0
counter2 = 5
while (counter1 < 5):
    star = ""
    c2 = counter2
    while (c2 > counter1):
        star = star + "*"
        c2 -= 1
    print(star)
    counter1 += 1
