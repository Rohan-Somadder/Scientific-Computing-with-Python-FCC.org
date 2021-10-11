"""
Program to add given time with extra hours and minutes and return the result.
"""

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]


def add_time(start, duration, day_name=None):

    new_time = start
    st_hrs, st_mins = map(int, new_time.split()[0].split(':'))
    hours, mins = map(int, duration.split(':'))
    day_time = new_time.split()[1]  # AM or PM
    extra = 0  # Extra hours for determinig the days

    if day_time == "PM":
        st_hrs += 12  # Converte to 24 hrs format

    if day_name:
        new_time += (", " + day_name)

    if day_name:
        day_name = day_name.lower().capitalize()

    if hours == 0 and mins == 0:
        return new_time

    if st_hrs + hours < 24:
        if st_mins + mins >= 60:
            st_hrs += (st_mins+mins)//60
            st_mins = st_mins + mins - (((st_mins + mins)//60)*60)
        else:
            st_mins = st_mins + mins
        st_hrs = st_hrs + hours

        if st_hrs <= 12:
            new_time = str(st_hrs)
        elif 12 < st_hrs < 24:
            new_time = str(st_hrs - 12)
        elif st_hrs >= 24:
            new_time = str(st_hrs - 24 if st_hrs != 24 else st_hrs - 12)
            extra += 1

        if st_mins < 10:
            new_time += ':0'+str(st_mins)
        else:
            new_time += ':'+str(st_mins)

        if 12 <= st_hrs < 24:
            new_time += ' PM'
        else:
            new_time += ' AM'

        if day_name:
            if extra == 1:
                new_time += ', ' + day_name + '(next day)'
            else:
                new_time += ', ' + day_name

    else:
        if st_mins + mins >= 60:
            hours += (st_mins+mins)//60
            st_mins = st_mins + mins - (((st_mins + mins)//60)*60)
        else:
            st_mins = st_mins + mins

        extra = hours//24
        hours = hours - extra*24
        st_hrs = st_hrs + hours

        if st_hrs < 12:
            new_time = str(st_hrs)
        elif 12 < st_hrs < 24:
            new_time = str(st_hrs - 12)
        elif st_hrs >= 24:
            new_time = str(st_hrs - 24 if st_hrs != 24 else st_hrs - 12)
            extra += 1

        if st_mins < 10:
            new_time += ':0'+str(st_mins)
        else:
            new_time += ':'+str(st_mins)

        if 12 <= st_hrs < 24:
            new_time += ' PM'
        else:
            new_time += ' AM'

        if day_name:
            new_time += ', ' + days[(days.index(day_name)+extra) % 7]
            if extra == 1:
                new_time += " (next day)"
            elif extra > 1:
                new_time += f" ({extra} days later)"
        else:
            if extra == 1:
                new_time += " (next day)"
            elif extra > 1:
                new_time += f" ({extra} days later)"

    return new_time
