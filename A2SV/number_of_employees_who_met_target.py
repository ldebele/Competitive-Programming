


def number_of_employees_who_met_the_target(hours, target):

    met_target = []

    for employee_hour in hours:
        if employee_hour >= target:
            met_target.append(employee_hour)

    return len(met_target)


if __name__ == "__main__":

    # hours = [0,1, 2, 3, 4]
    # target = 2

    hours = [5, 1, 4, 2, 2]
    target = 6

    met_target = number_of_employees_who_met_the_target(hours, target)
    print(met_target)
