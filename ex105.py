# Analyzing student's grade
datas = {}


def grade(*n, sit=False):
    """
    -> Function to analyze grades and situations of many students.
    :param n: Student's grades
    :param sit: Analyze the class situation
    :return: Dictionary with a lot of information about the class
    """
    # Quantity of grades
    for count in range(0, len(n)):
        datas['grades_quantity'] = count + 1
    # Biggest grade
    count2 = biggest = 0
    for value in n:
        if count2 == 0:
            biggest = value
        else:
            if biggest < value:
                biggest = value
        count2 += 1
    datas['biggest_grade'] = biggest
    # Lower grade
    count3 = lowest = 0
    for c in n:
        if count3 == 0:
            lowest = c
        else:
            if lowest > c:
                lowest = c
        count3 += 1
    datas['Lowest_grade'] = lowest
    # Average of grades
    average = sum(n) / len(n)
    average_formatted = "{:.2f}".format(average)
    datas['average_grade'] = average_formatted
    # Optional character
    if sit:
        if average < 6:
            datas['situation'] = 'Disapproved'
        elif 6 <= average < 7:
            datas['situation'] = 'Reasonable'
        else:
            datas['situation'] = 'Approved'
    return datas


# Main Program
answer = grade(5, 3, 5, sit=True)
print(answer)
