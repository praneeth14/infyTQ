#PF-Assgn-22
def find_leap_years(given_year):

    # Write your logic here
    list_of_leap_years=[]
    year=given_year
    count=0
    while(count!=15):

        if(year%400==0):
            list_of_leap_years.append(year)
            count+=1
        elif(year%100==0):
            pass
        elif(year%4==0):
            list_of_leap_years.append(year)
            count+=1
        else:
            pass
        year += 1

    return list_of_leap_years

list_of_leap_years=find_leap_years(1684)
print(list_of_leap_years)