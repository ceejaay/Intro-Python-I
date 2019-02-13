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

cal = calendar.yeardayscalendar(2019)
print(cal)

arg_length = len(sys.argv)
if arg_length == 1:
    print('the current month')
elif arg_length == 2:
    year = sys.argv[1]
    print('the selected month')
elif arg_length == 3:
    month = sys.argv[1]
    year = sys.argv[2]
    print('the selected month and year')





# day = calendar.TextCalendar(4)
# year = day.formatmonth(2011, 3, 3)
# print(year)
