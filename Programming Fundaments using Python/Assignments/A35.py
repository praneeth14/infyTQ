# PF-Assgn-35

# Global variable
list_of_marks = (12, 18, 25, 24, 2, 5, 18, 20, 20, 21)


def find_more_than_average():
    avg_count = 0
    avg = sum(list_of_marks) / 10
    for mark in list_of_marks:
        if mark > avg:
            avg_count += 1
    return (avg_count * 10)


def sort_marks():
    marks_list = list(list_of_marks)
    marks_list.sort()
    return marks_list


def generate_frequency():
    frequency_list = []
    for i in range(0, 26):
        frequency_list.append(list_of_marks.count(i))
    return frequency_list


print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
