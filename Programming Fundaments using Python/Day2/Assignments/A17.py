# PF-Tryout

def find_new_salary(current_salary, job_level):
    # write your logic here
    if (job_level == 3):
        hike_per = 15
    elif (job_level == 4):
        hike_per = 7
    elif (job_level == 5):
        hike_per == 5
    else:
        hike_per == 0

    new_salary = int(current_salary + ((hike_per * current_salary) / 100))

    return new_salary


# provide different values for current_salary and job_level and test yor program
new_salary = find_new_salary(15000, 3)
print(new_salary)
