#!/usr/bin/env python

"""
http://www.pythonchallenge.com/pc/def/channel.html
"""

import requests
import zipfile
import StringIO
import re
import sys
import string

nothing = 90052
pat = re.compile('Next nothing is ([0-9]*)')
r = requests.get('http://www.pythonchallenge.com/pc/def/channel.zip')
s = StringIO.StringIO(r.content)
z = zipfile.ZipFile(s, "r")
d = {}
letters = []
for i in z.infolist():
  d[i.filename] = i.comment
#  sys.stdout.write(i.comment)
while True:
  filename = '%s.txt' % nothing
  f = z.open(filename)
  t = f.read()
#  print t
  sys.stdout.write(d[filename])
  if d[filename] in string.letters and d[filename] not in letters:
    letters.append(d[filename])
  m = pat.search(t)
  if m:
    nothing = int(m.groups()[0])
#    print 'Next: %d' % nothing
  else:
#    print t
    break
print "".join(letters)
