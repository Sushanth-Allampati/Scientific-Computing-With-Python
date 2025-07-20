def add_time(start, duration, day=None):
    # Days of the week in order
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Split start time and period
    time_part, period = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))

    # Convert to 24-hour format for easier calculations
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    if period == 'AM' and start_hour == 12:
        start_hour = 0

    # Split duration time
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Add minutes and hours
    total_minutes = start_minute + duration_minute
    extra_hour = total_minutes // 60
    final_minute = total_minutes % 60

    total_hours = start_hour + duration_hour + extra_hour
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24

    # Convert back to 12-hour format
    if final_hour_24 == 0:
        final_hour = 12
        final_period = 'AM'
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        final_period = 'AM'
    elif final_hour_24 == 12:
        final_hour = 12
        final_period = 'PM'
    else:
        final_hour = final_hour_24 - 12
        final_period = 'PM'

    # Construct result time string
    new_time = f"{final_hour}:{final_minute:02d} {final_period}"

    # Add day of the week if provided
    if day:
        day_index = days_of_week.index(day.capitalize())
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    # Add days later info
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
add_time("3:00 PM", "3:10")
add_time("11:30 AM", "2:32", "Monday")