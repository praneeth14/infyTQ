# PF-Exer-7

def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost = 0
    # Write your logic here
    rate_per_adult = 37550.0
    rate_per_child = (rate_per_adult / 3)
    ticket_cost = no_of_adults * rate_per_adult + no_of_children * rate_per_child
    service_cost = (ticket_cost * 7) / 100
    total_cost_before_discount = ticket_cost + service_cost
    discount = (total_cost_before_discount * 10) / 100
    total_ticket_cost = (total_cost_before_discount - discount)
    return total_ticket_cost


# Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost = calculate_total_ticket_cost(5, 2)
print("Total Ticket Cost:", total_ticket_cost)
