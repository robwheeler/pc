#!/usr/bin/env python

"""
http://www.pythonchallenge.com/pc/return/bull.html
a = [1, 11, 21, 1211, 111221, ...]
len(a[30]) = ?
"""


def sayit(x):
  s = str(x)
  count = 0
  last = ''
  current = ''
  solution = []
  for i in xrange(len(s)):
    if s[i] == last:
      count += 1
    else:
      if last:
        solution.extend((str(count), last))
      count = 1
      last = s[i]
  if last:
    solution.extend((str(count), last))
  return "".join(solution)

a = [1]
for x in xrange(1, 31):
  a.append(sayit(a[x-1]))
print 'http://www.pythonchallenge.com/pc/return/%s.html' % len(a[30])
