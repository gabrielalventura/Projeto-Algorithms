def study_schedule(permanence_period, target_time):
    more_students = 0

    if (
        not permanence_period
        or type(permanence_period) != list
        or not target_time
    ):
        return None

    for time in permanence_period:

        if time[0] <= target_time <= time[1]:
            more_students += 1

    return more_students
