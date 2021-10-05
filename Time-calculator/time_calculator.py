days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
time = ["AM", "PM"]


def add_hours(current_hours, add_hours, ts=None, day=None):
    # Todo: return [current_hours,ts] after calculations
    if 12 <= add_hours + current_hours < 24:
        current_hours = add_hours + current_hours - 12
        if ts:
            ts = time[(time.index(ts) + 1) % 2]
    elif add_hours + current_hours >= 24:
        current_hours = add_hours + current_hours - 24
        if day:
            day = days[(days.index(day)+1) % 7]
    return [current_hours, ts, day]


def add_time(start, duration, Day=None):

    new_time = start
    new_hrs, new_mins = map(int, new_time.split()[0].split(':'))
    hours, mins = map(int, duration.split(':'))
    day_time = new_time.split()[1]  # AM or PM
    if Day:
        new_time += (", " + Day)
    if Day:
        Day = Day.lower().capitalize()

    if hours == '0' and mins == '00':
        return new_time
    elif hours < 24:
        if new_mins + mins >= 60:
            new_hrs += (new_mins+mins)//60
            mins = new_mins + mins - (((new_mins + mins)//60)*60)
        else:
            mins = mins + new_mins

        hours, day_time, Day = map(
            str, add_hours(hours, new_hrs, day_time, Day))
        Day = None if Day == 'None' else Day
        new_time = (str(hours) if int(hours) >= 10 else '0' + str(hours)) + ':' + (str(mins) if mins >= 10 else '0'+str(mins)
                                                                                   ) + ' ' + str(day_time) + ((', ' + Day) if Day else '')
        # Todo : How to prevent (next day) from the text
        #! Working incorrectly
        if Day != new_time.split()[1]:
            new_time += ' (next day)'

    elif hours == 24:
        if Day:
            Day = days[(days.index(Day)+1) % 7]
            new_time += ", " + Day + " (next day)"
        else:
            new_time += ", (next day)"

    else:
        time = hours//24
        hours = hours - (time*24)
        if new_mins + mins >= 60:
            new_hrs += (new_mins+mins)//60
            mins = new_mins + mins - (((new_mins + mins)//60)*60)
        else:
            mins = mins + new_mins

        hours, day_time, Day = map(
            str, add_hours(hours, new_hrs, day_time, Day))
        Day = None if Day == 'None' else Day
        new_time = (str(hours) if int(hours) >= 10 else '0'+str(hours)) + ':' + (str(mins) if mins >= 10 else '0'+str(mins)) + \
            ' ' + str(day_time) + ', ' + (Day if Day else '') + \
            (' (next day)' if time == 1 else f' ({time} days later)')

    return new_time


#print(add_time("3:30 PM", "2:12"))
