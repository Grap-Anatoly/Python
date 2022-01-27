# Often in data science we need analysis which is based on temporal values.
# Python can handle the various formats of date and time gracefully.
# The datetime library provides necessary methods and functions to handle the following scenarios.
#
# Date Time Representation
# Date Time Arithmetic
# Date Time Comparison


# A date and its various parts are represented by using different datetime functions.
# Also, there are format specifiers which play a role in displaying the alphabetical parts of a date
# like name of the month or week day.

import datetime

print('The Date Today is  :', datetime.datetime.today())

date_today = datetime.date.today()
print (date_today)
print ('This Year   :', date_today.year)
print ('This Month    :', date_today.month)
print ('Month Name:',date_today.strftime('%B'))
print ('This Week Day    :', date_today.day)
print ('Week Day Name:',date_today.strftime('%A'))

# For calculations involving dates we store the various dates into variables
# and apply the relevant mathematical operator to these variables.

# Capture the First Date
day1 = datetime.date(2018, 2, 12)
print('day1:', day1.ctime())

# Capture the Second Date
day2 = datetime.date(2017, 8, 18)
print('day2:', day2.ctime())

# Find the difference between the dates
print('Number of Days:', day1 - day2)

date_today = datetime.date.today()

# Create a delta of Four Days
no_of_days = datetime.timedelta(days=4)

# Use Delta for Past Date
before_four_days = date_today - no_of_days
print('Before Four Days:', before_four_days)

# Use Delta for future Date
after_four_days = date_today + no_of_days
print('After Four Days:', after_four_days )

# Date and time are compared using logical operators.
# But we must be careful in comparing the right parts of the dates with each other.

date_today  = datetime.date.today()

print('Today is: ', date_today)
# Create a delta of Four Days
no_of_days = datetime.timedelta(days=4)

# Use Delta for Past Date
before_four_days = date_today - no_of_days
print('Before Four Days:', before_four_days)

after_four_days =  date_today + no_of_days

date1 = datetime.date(2018,4,4)

print('date1:',date1)

if date1 == before_four_days :
    print ('Same Dates')
if date_today > date1:
    print ('Past Date')
if date1 < after_four_days:
    print ('Future Date')
