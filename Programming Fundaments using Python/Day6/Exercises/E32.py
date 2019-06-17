# PF-Exer-32

def human_pyramid(no_of_people):
    if no_of_people == 1:
        return 50
    else:
        return no_of_people * 50 + human_pyramid(no_of_people - 2)


def find_maximum_people(max_weight):
    no_of_people = 1
    # write your logic here. You may invoke recursive function human_pyramid() wherever applicable
    while (human_pyramid(no_of_people) <= max_weight):
        no_of_people+=2
    no_of_people-=2 #while loop increments the no_of_people one time extra before loop terminates so decreasing it
    return no_of_people


# Provide different values for max_weight and test your program
max_people = find_maximum_people(1050)
print(max_people)
