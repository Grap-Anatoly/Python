# The datetime module supplies classes for manipulating dates and times.

# Date and time objects may be categorized as “aware” or “naive” depending on whether or not they include timezone information.

# Aware object can locate itself relative to other aware objects.
# An aware object represents a specific moment in time that is not open to interpretation.
#
# A naive object does not contain enough information to unambiguously locate itself relative to other date/time objects.

import datetime

# Constants

print(datetime.MINYEAR)

print(datetime.MAXYEAR)

# Types

# class datetime.date
# An idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect.
# Attributes: year, month, and day.

# class datetime.time
# An idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds. (There is no notion of “leap seconds” here.)
# Attributes: hour, minute, second, microsecond, and tzinfo.

# class datetime.datetime
# A combination of a date and a time.
# Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.

# class datetime.timedelta
# A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.

# class datetime.tzinfo
# An abstract base class for time zone information objects.
# These are used by the datetime and time classes to provide a customizable notion of time adjustment (for example, to account for time zone and/or daylight saving time).

# class datetime.timezone
# A class that implements the tzinfo abstract base class as a fixed offset from the UTC.


# The date, datetime, time, and timezone types share these common features:

# Objects of these types are immutable.
# Objects of these types are hashable, meaning that they can be used as dictionary keys.
# Objects of these types support efficient pickling via the pickle module.

# Objects of the date type are always naive.

# An object of type time or datetime may be aware or naive.

# A datetime object d is aware if both of the following hold:

# d.tzinfo is not None
# d.tzinfo.utcoffset(d) does not return None
# Otherwise, d is naive.

# A time object t is aware if both of the following hold:
# t.tzinfo is not None
# t.tzinfo.utcoffset(None) does not return None.
# Otherwise, t is naive.

# A timedelta object represents a duration, the difference between two dates or times.

from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    minutes=5,
    hours=8,
    weeks=2
)

print(delta)

d = timedelta(microseconds=-1)

print(d)

# A date object represents a date (year, month and day) in an idealized calendar,
# the current Gregorian calendar indefinitely extended in both directions.

print(datetime.date(2022,11,21))

print(datetime.date.today())
