days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
time = ["AM", "PM"]


def add_hours(current_hours, add_hours, ts=None):
    # Todo: return [current_hours,ts] after calculations
    pass


def add_time(start, duration, day=None):

    new_time = start
    new_hrs, new_mins = map(int, new_time.split()[0].split(':'))
    hours, mins = map(int, duration.split(':'))
    day_time = new_time.split()[1]  # AM or PM

    if day:
        day = day.lower().capitalize()

    if hours == '0' and mins == '00':
        return new_time
    elif hours < 24:
        if new_mins + mins >= 60:
            new_hrs += (new_mins+mins)//60
            mins = new_mins + mins - (((new_mins + mins)//60)*60)
        else:
            mins = mins + new_mins

        hours, day_time = map(int, add_hours(hours, new_hrs, day_time))

    elif hours == 24:
        if day:
            day = days[(days.index(day)+1) % 7]
            new_time += ", " + day + " (next day)"
        else:
            new_time += ", (next day)"

    else:
        time = hours//24
        hours = hours - (time*24)
        # TODO: Do the same as hours < 24

    return new_time


print(add_time("11:06 PM", "24:00", "sunday"))
