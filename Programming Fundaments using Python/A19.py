# PF-Assgn-19
def calculate_distance_charge(d):
    if (d <= 3):
        charge = 0
    elif (d > 3 and d <= 6):
        charge = (d - 3) * 3
    else:
        d = d - 3
        charge = (d - 3) * 6 + 9
    return charge


def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
    bill_amount = -1
    charge_per_plate = 0
    input_flag = 1
    if (food_type == "V"):
        charge_per_plate = 120
    elif (food_type == "N"):
        charge_per_plate = 150
    else:
        input_flag = 0

    if (quantity_ordered < 1):
        input_flag = 0

    if (distance_in_kms < 1):
        input_flag == 0
    else:
        dis_charge = calculate_distance_charge(distance_in_kms)
        bill_amount = charge_per_plate * quantity_ordered + dis_charge

    if (input_flag == 0):
        bill_amount = -1
    # write your logic here
    return bill_amount


# Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount = calculate_bill_amount("N", 1, 7)
print(bill_amount)