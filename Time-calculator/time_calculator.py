"""
Program to add given time with extra hours and minutes and return the result.
"""

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
time = ["AM", "PM"]


def add_hours(current_hours, add_hours, ts=None, day=None):

    # Todo: return [current_hours,ts] after calculations
    if current_hours + add_hours < 12:
        current_hours = current_hours + add_hours

    elif 12 <= add_hours + current_hours < 24:
        current_hours = add_hours + current_hours - 12
        if ts:
            ts = time[(time.index(ts) + 1) % 2]

    elif add_hours + current_hours >= 24:
        current_hours = add_hours + current_hours - 24
        if day:
            day = days[(days.index(day)+1) % 7]

    return [current_hours, ts, day]


def add_time(start, duration, day_name=None):

    new_time = start
    new_hrs, new_mins = map(int, new_time.split()[0].split(':'))
    hours, mins = map(int, duration.split(':'))
    day_time = new_time.split()[1]  # AM or PM

    if day_name:
        new_time += (", " + day_name)
    # print(new_time,hours,mins)
    if day_name:
        day_name = day_name.lower().capitalize()

    if hours == 0 and mins == 0:
        return new_time

    elif hours < 24:
        if new_mins + mins >= 60:
            new_hrs += (new_mins+mins)//60
            mins = new_mins + mins - (((new_mins + mins)//60)*60)

        else:
            mins = mins + new_mins

        hours, day_time, day_name = map(
            str, add_hours(hours, new_hrs, day_time, day_name))
        day_name = None if day_name == 'None' else day_name
        new_time = hours + ':' + (str(mins) if mins >= 10 else '0'+str(mins)
                                  ) + ' ' + str(day_time) + ((', ' + day_name) if day_name else '')
        # Todo : How to prevent (next day) from the text
        #! Working incorrectly
        print(new_time.split()[1])
        if day_name != new_time.split()[1] and day_name is not None:
            print(new_time, day_name)
            new_time += ' (next day)'

    elif hours == 24:
        if day_name:
            day_name = days[(days.index(day_name)+1) % 7]
            new_time += ", " + day_name + " (next day)"

        else:
            new_time += ", (next day)"

    else:
        extra = hours//24
        hours = hours - (extra*24)
        if new_mins + mins >= 60:
            new_hrs += (new_mins+mins)//60
            mins = new_mins + mins - (((new_mins + mins)//60)*60)

        else:
            mins = mins + new_mins

        hours, day_time, day_name = map(
            str, add_hours(hours, new_hrs, day_time, day_name))
        day_name = None if day_name == 'None' else day_name
        new_time = hours + ':' + (str(mins) if mins >= 10 else '0' + str(mins)) + \
            ' ' + str(day_time) + ', ' + (day_name if day_name else '')
        if not day_name:
            new_time += (' (next day)' if extra ==
                         1 else f' ({extra} days later)')

    return new_time


print(add_time("9:15 PM", "5:30"))  # == "2:45 AM (next day)")
