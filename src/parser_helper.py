# TODO: write unit test for this
def get_hours(temp_hours):
    time = []
    for day, hours in temp_hours.items():  # order will be from Mon->Sun
        if hours == 'x':
            time.append('NA')
        else:
            time.append(hours)
    return time
