# PF-Assgn-29
def calculate(distance, no_of_passengers):
    fuel_price = 70
    mileage = 10
    ticket_price = 80
    total_fuel_price = (distance / mileage) * fuel_price
    total_ticket_price = (no_of_passengers * ticket_price)

    if (total_ticket_price > total_fuel_price):
        return (total_ticket_price - total_fuel_price)
    else:
        return -1


# Provide different values for distance, no_of_passenger and test your program
distance = 20
no_of_passengers = 50
print(calculate(distance, no_of_passengers))
