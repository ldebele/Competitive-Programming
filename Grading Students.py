def gradingStudents(grades):

    for i in range(len(grades)):

        upper_grade = ((grades[i] // 5)*5) + 5

        if grades[i] > 40:
            if (upper_grade - grades[i]) < 3:
                grades[i] = upper_grade

    return grades


