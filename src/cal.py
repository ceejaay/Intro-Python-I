"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

"""


import sys
import calendar
from datetime import datetime

# cal = calendar.Calendar

# print(cal.yeardatescalendar(2019, 6))
cal = calendar.TextCalendar(4)
# print(cal.formatmonth(2011, 3, 3))

# Ok, so we need to convert the text to an integer. There may be a thing in python date/time that will do that.

# def text_to_int(argument):
#     for item in argument:
#         if



arg_length = len(sys.argv)
if arg_length == 1:
    print(cal.formatmonth(2019, 2, 3))
elif arg_length == 2:
    year = sys.argv[1]
    print(cal.formatmonth(year, 2, 3))
elif arg_length == 3:
    month = sys.argv[1]
    year = sys.argv[2]
    print(year, month, 3)





# year = day.formatmonth(2011, 3, 3)
