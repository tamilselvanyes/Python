from math import ceil, floor
from datetime import datetime, timedelta
from enum import Enum


class TimeGrain(str, Enum):
    HOUR = "hour"
    WEEKDAY = "weekday"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    QUARTER = "quarter"
    YEAR = "year"
    NONE = None


MonthNumber = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}

WeekdayNumber = {
    "monday": 6,
    "tuesday": 5,
    "wednesday": 4,
    "thursday": 3,
    "friday": 2,
    "saturday": 1,
    "sunday": 0,
}


def get_year_based_on_calendar(day, start_month_number):
    year = day.year

    def to_month(day):
        return day.month

    if to_month(day) < start_month_number:
        return year - 1
    else:
        return year


def get_quarter_based_on_calendar(day, start_month_number):
    return floor(((12 + day.month - start_month_number) % 12) / 3) + 1


def calculate_quarter_dates(year, quarter, month_number):
    if quarter == 1:
        start_month = month_number
        end_month = month_number + 3
        if end_month > 12:
            year += 1
        start_date = datetime(year, start_month, 1)
        end_date = datetime(year, end_month % 12, 1) + timedelta(days=-1)
    elif quarter == 2:
        start_month = month_number + 3
        end_month = month_number + 6
        if start_month > 12 or end_month > 12:
            year += 1
        start_date = datetime(year, start_month % 12, 1)
        end_date = datetime(year, end_month % 12, 1) + timedelta(days=-1)
    elif quarter == 3:
        start_month = month_number + 6
        end_month = month_number + 9
        if start_month > 12 or end_month > 12:
            year += 1
        start_date = datetime(year, (month_number + 6) % 12, 1)
        end_date = datetime(year, (month_number + 9) % 12, 1) + timedelta(days=-1)
    elif quarter == 4:
        start_month = month_number + 6
        end_month = month_number + 12
        if start_month > 12 or end_month > 12:
            year += 1
        start_date = datetime(year, (month_number + 9) % 12, 1)
        end_date = datetime(year, (month_number + 12) % 12, 1) + timedelta(days=-1)
    else:
        raise ValueError("Invalid quarter value")

    return start_date, end_date


def get_week_number_on_calendar(required_day, start_month, start_week):
    start_week_number = WeekdayNumber[start_week]
    start_month_number = MonthNumber[start_month]
    current_year = get_year_based_on_calendar(required_day, start_month_number)
    year_start_date = datetime(current_year, start_month_number, 1)
    current_week_day_number = year_start_date.isoweekday()
    calculated_date = required_day + timedelta((current_week_day_number + start_week_number) % 7 + 1)
    days_passed = (calculated_date - year_start_date).days
    return ceil(days_passed / 7)


# week number here is our the opposite conviction monday 6
def calculate_week_range_dates(start_month_of_year, week_start, required_year, required_week_number):
    start_month = MonthNumber.get(start_month_of_year)
    start_date = datetime.strptime(f'{required_year}-{start_month:02d}-01', '%Y-%m-%d')
    start_weekday = start_date.weekday()
    # Calculate the number of days to adjust based on the start_week_day
    start_weekday_mapping = {'sunday': 6, 'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4,
                             'saturday': 5}
    days_to_adjust = (start_weekday_mapping[week_start] - start_weekday) % 7

    if days_to_adjust == 0:
        start_date += timedelta(days=(required_week_number - 1) * 7 + days_to_adjust)
        end_date = start_date + timedelta(days=6, hours=23, minutes=59, seconds=59)
    else:
        # week already started from 1
        if required_week_number - 1 == 0:
            end_date = start_date + timedelta(days=days_to_adjust - 1, hours=23, minutes=59, seconds=59)
        else:
            start_date += timedelta(days=(required_week_number - 2) * 7 + days_to_adjust)
            end_date = start_date + timedelta(days=6, hours=23, minutes=59, seconds=59)
    return start_date, end_date


def calculate_relative_year_dates(start_month, relative_string):
    day = datetime.now()
    year = day.year
    month_number = MonthNumber[start_month]

    def to_month(day):
        return day.month

    def to_year(day, month_number):
        if to_month(day) < month_number:
            return year - 1
        else:
            return year

    if (relative_string == 'current_year'):
        start_date = datetime(to_year(day, month_number), month_number, 1)
        end_date = day
    elif (relative_string == 'previous_year'):
        start_date = datetime(to_year(day, month_number) - 1, month_number, 1)
        end_date = datetime(to_year(day, month_number), month_number, 1)
    else:
        start_date = datetime(to_year(day, month_number) - 2, month_number, 1)
        end_date = datetime(to_year(day, month_number), month_number, 1)
    return start_date, end_date


def calculate_relative_quarter_dates(start_month, relative_string):
    day = datetime.now()
    month_number = MonthNumber[start_month]
    current_quarter = get_quarter_based_on_calendar(day, month_number)
    current_year = get_year_based_on_calendar(day, month_number)

    if (relative_string == 'current_quarter'):
        return calculate_quarter_dates(current_year, current_quarter, month_number)
    elif (relative_string == 'previous_quarter'):
        if current_quarter - 1 == 0:
            return calculate_quarter_dates(current_year - 1, 4, month_number)
        else:
            return calculate_quarter_dates(current_year, current_quarter - 1, month_number)
    else:
        previous_year = current_year - 1
        last_quarter = 4
        if current_quarter - 2 == 0:
            start_date = calculate_quarter_dates(previous_year, 4, month_number)[0]
            end_date = calculate_quarter_dates(current_year, 1, month_number)[1]
            return start_date, end_date
        elif current_quarter - 2 == -1:
            start_date = calculate_quarter_dates(previous_year, 3, month_number)[0]
            end_date = calculate_quarter_dates(previous_year, 4, month_number)[1]
            return start_date, end_date
        else:
            start_date = calculate_quarter_dates(current_year, current_quarter - 2, month_number)[0]
            end_date = calculate_quarter_dates(current_year, current_quarter - 1, month_number)[1]
            return start_date, end_date


def calculate_relative_month_dates(relative_string):
    day = datetime.now()
    current_year = day.year
    current_month = day.month

    if (relative_string == 'current_month'):
        start_date = datetime(current_year, current_month, 1)
        end_date = day
    elif (relative_string == 'previous_month'):
        last_month = 12
        previous_year = current_year - 1
        if current_month - 1 == 0:
            start_date = datetime(previous_year, last_month, 1)
            end_date = datetime(current_year, current_month, 1)
        else:
            start_date = datetime(current_year, current_month - 1, 1)
            end_date = datetime(current_year, current_month, 1)
    else:
        previous_year = current_year - 1
        last_month = 12

        if current_month - 2 == 0:
            start_date = datetime(previous_year, last_month, 1)
            end_date = datetime(current_year, 2, 1)
        elif current_month - 2 == -1:
            start_date = datetime(previous_year, last_month - 1, 1)
            end_date = datetime(current_year, 1, 1)
        else:
            start_date = datetime(current_year, current_month - 2, 1)
            end_date = datetime(current_year, current_month, 1)

    return start_date, end_date


def calculate_relative_week_dates(start_month, start_week, relative_string):
    today_date = datetime.now()
    current_year = get_year_based_on_calendar(today_date, MonthNumber[start_month])
    current_week = get_week_number_on_calendar(today_date, start_month, start_week)

    if (relative_string == 'current_week'):
        return calculate_week_range_dates(start_month, start_week, current_year, current_week)
    elif (relative_string == 'previous_week'):
        previous_year = current_year - 1
        if current_week - 1 == 0:
            last_day_previous_year = datetime.strptime(f'{current_year}-{start_month:02d}-01', '%Y-%m-%d') - timedelta(
                days=1)
            last_week_number = get_week_number_on_calendar(last_day_previous_year)
            return calculate_week_range_dates(start_month, start_week, previous_year, last_week_number)
        else:
            return calculate_week_range_dates(start_month, start_week, current_year, current_week - 1)
    else:
        previous_year = current_year - 1
        if current_week - 2 == 0:
            last_day_previous_year = datetime.strptime(f'{current_year}-{start_month:02d}-01', '%Y-%m-%d') - timedelta(
                days=1)
            last_week_number = get_week_number_on_calendar(last_day_previous_year)
            start_date = calculate_week_range_dates(start_month, start_week, previous_year, last_week_number)[0]
            end_date = calculate_week_range_dates(start_month, start_week, current_year, 1)[1]
        elif current_week - 2 == -1:
            last_day_previous_year = datetime.strptime(f'{current_year}-{start_month:02d}-01', '%Y-%m-%d') - timedelta(
                days=1)
            last_week_number = get_week_number_on_calendar(last_day_previous_year)
            start_date = calculate_week_range_dates(start_month, start_week, previous_year, last_week_number - 1)[0]
            end_date = calculate_week_range_dates(start_month, start_week, previous_year, last_week_number - 1)[1]
        else:
            start_date = calculate_week_range_dates(start_month, start_week, current_year, current_week - 2)[0]
            end_date = calculate_week_range_dates(start_month, start_week, current_year, current_week - 1)[1]

    return start_date, end_date


def calculate_relative_day_dates(relative_string):
    time_now = datetime.now()
    if relative_string == 'today':
        start_date = time_now.replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = time_now

    elif relative_string == 'yesterday':
        end_date = time_now.replace(hour=0, minute=0, second=0, microsecond=0)
        start_date = end_date - timedelta(days=1)

    else:
        # last_2_days
        end_date = time_now.replace(hour=0, minute=0, second=0, microsecond=0)
        start_date = end_date - timedelta(days=2)

    return start_date, end_date


def calculate_relative_hour_dates(relative_string):
    time_now = datetime.now()
    if relative_string == 'current_hour':
        start_date = time_now.replace(minute=0, second=0, microsecond=0)
        end_date = time_now
    elif relative_string == 'previous_hour':
        end_date = time_now.replace(minute=0, second=0, microsecond=0)
        start_date = end_date - timedelta(hours=1)
    else:
        end_date = time_now.replace(minute=0, second=0, microsecond=0)
        start_date = end_date - timedelta(hours=2)
    return start_date, end_date


def get_relative_date_range(calendar_start_month, calendar_start_week, time_grain, relative_string):
    if time_grain == TimeGrain.YEAR:
        return calculate_relative_year_dates(calendar_start_month, relative_string)
    elif time_grain == TimeGrain.QUARTER:
        return calculate_relative_quarter_dates(calendar_start_month, relative_string)
    elif time_grain == TimeGrain.MONTH:
        return calculate_relative_month_dates(relative_string)
    elif time_grain == TimeGrain.WEEK:
        return calculate_relative_week_dates(calendar_start_month, calendar_start_week, relative_string)
    elif time_grain == TimeGrain.DAY:
        return calculate_relative_day_dates(relative_string)
    else:
        return calculate_relative_hour_dates(relative_string)


print(get_relative_date_range("november", "monday", "year", "previous_year"))