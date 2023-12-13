import datetime

start_date = datetime.date(2017, 2, 16)
end_date = datetime.date(2017, 2, 16)
start_time = datetime.time(4, 30, 0)
end_time = datetime.time(4, 30, 17)

# Above, there are four variables: start_date, end_date,
# start_time, and end_time. start_date and start_time together
# represent a certain time on a certain date, and end_date and
# end_time represent a different time on a different date.
#
# Add some code below that will print True if the end time
# occurs after the start time. Print False if the end time
# occurs before the start time. For example, 11:15:00 on
# 01/01/2017 would be before 09:00:00 on 01/05/2017, which
# would be before 11:25:00 on 01/05/2017.
#
# Note that you may use dot notation to access the individual
# parts of the dates and times. You can access the hour,
# minute, and seconds from start_time with start_time.hour,
# start_time.minute, and start_time.second. You can access
# the year, month, and day of start_date with
# start_date.year, start_date.month, and start_date.day. You
# can use the same syntax to access the parts of end_date.
# Note that Python uses 24-hour time.
#
# Hint: You may use conditionals to solve this if you want,
# but you don't need to.
#
# Hint 2: You can use relational operators with both dates
# and times. start_time < end_time is True if start_time is
# before end_time. start_date >= end_date is True if
# start_date is later than end_date, or the same date. With
# this, you can avoid using dot notation altogether if
# you'd like.


# Add your code here!
print(start_date <= end_date and start_time < end_time)
