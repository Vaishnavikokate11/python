# find total avg and highest marks from a list in for student

marks = [45,67,89,76,79]

total = 0
highest = marks[0]

for mark in marks:
    total = mark + total 
    if (mark > highest):
        highest = mark
    avg = total / len(marks)
    print(f"total marks is {total} \n Avg marks is {avg} \n and highest makrs is {highest}")
