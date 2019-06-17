# PF-Exer-30

def find_average(mark_list):
    try:
        total = 0
        for i in range(0, len(mark_list)):
            total += mark_list[i]
        marks_avg = total / len(mark_list)
        return marks_avg
    except NameError: #normal handling
        print("Name Error (undefined name is used)")
    except TypeError: #case 1
        print("unsupported operand types")
    except ValueError: #case 2
        print("Value Error")
    except ZeroDivisionError: #case 3
        print("divided by zero")
    except IndexError: #case 4
        print("list index out of range")
    except:#default
        print("something error occured")


m_list=[1,2,3,4]
print("Average marks:", find_average(m_list))
