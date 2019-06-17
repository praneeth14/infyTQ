# PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list, medical_speciality):
    # write your logic here
    max_speciality=''
    max_visited=0
    for key in medical_speciality.keys():
        visited=patient_medical_speciality_list.count(key)
        if(visited>max_visited):
            max_visited=visited
            max_speciality=key

    speciality=medical_speciality[max_speciality]

    return speciality


# provide different values in the list and test your program
patient_medical_speciality_list = [301, 'P', 302, 'P', 305, 'P', 401, 'E', 656, 'E']
medical_speciality = {"P": "Pediatrics", "O": "Orthopedics", "E": "ENT"}
speciality = max_visited_speciality(patient_medical_speciality_list, medical_speciality)
print(speciality)
