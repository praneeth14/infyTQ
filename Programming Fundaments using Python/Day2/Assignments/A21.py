# PF-Tryout
def isLeafYear(y):
    if (y % 400 == 0):
        return True
    elif (y % 100 == 0):
        return False
    elif (y % 4 == 0):
        return True
    else:
        return False


def generate_next_date(day, month, year):
    # Start writing your code here
    next_day = day
    next_month = month
    next_year = year
    if (month in (1, 3, 5, 7, 8, 10, 12)):
        month_length = 31
    elif (month == 2):
        if (isLeafYear(year)):
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30

    if (day < month_length):
        next_day = day + 1
    else:
        next_day = 1
        if (month == 12):
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1

    print(next_day, "-", next_month, "-", next_year, sep="")


generate_next_date(30, 6, 2015)
