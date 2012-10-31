#!/usr/bin/env python

"""
http://www.pythonchallenge.com/pc/return/uzi.html
"""

import calendar
c = calendar.TextCalendar()
for x in xrange(100):
  year = 1006 + 10 * x
  if calendar.isleap(year):
    if calendar.weekday(year, 1, 1) == 3:
      print c.formatmonth(year, 1)

# Mozart was born on January 26th, 1756
