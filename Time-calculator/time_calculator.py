def add_time(start, duration, day=None):

    new_time = start
    hours, mins = map(int, duration.split(':'))

    if hours == '0' and mins == '00':
        return new_time
    elif int(hours) < 24:
        pass
    elif int(hours) == 24:
        pass
    else:
        pass
    return new_time


print(add_time("11:06 PM", "2:02"))
