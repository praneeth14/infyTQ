# PF-Exer-22

def generate_ticket(airline, source, destination, no_of_passengers):
    ticket_number_list = []
    # Write your logic here
    for i in range(1, no_of_passengers + 1):
        ticket = airline + ":" + source[:3] + ":" + destination[:3] + ":" + str(100 + i)
        ticket_number_list.append(ticket)
    ticket_number_list = ticket_number_list[-5:]
    # Use the below return statement wherever applicable
    return ticket_number_list


# Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI", "Bangalore", "London", 7))
