# This module allows you to output calendars like the Unix cal program,
# and provides additional useful functions related to the calendar.

import calendar

print(calendar.calendar(2022))

# a = calendar.Calendar.itermonthdays(2022,3,"June")
# print(a)

# iterweekdays()
# Return an iterator for the week day numbers that will be used for one week.
# The first value from the iterator will be the same as the value of the firstweekday property.

# itermonthdates(year, month)
# Return an iterator for the month month (1–12) in the year year.
# This iterator will return all days (as datetime.date objects)
# for the month and all days before the start of the month or after the end of the month that are required to get a complete week.

# itermonthdays(year, month)
# Return an iterator for the month month in the year year similar to itermonthdates(), but not restricted by the datetime.date range. Days returned will simply be day of the month numbers.
# For the days outside of the specified month, the day number is 0.

print(calendar.TextCalendar())