#!/usr/bin/env python

"""
http://www.pythonchallenge.com/pc/def/channel.html
"""

import requests
import zipfile
import StringIO
import re
import sys

nothing = 90052
pat = re.compile('Next nothing is ([0-9]*)')
r = requests.get('http://www.pythonchallenge.com/pc/def/channel.zip')
s = StringIO.StringIO(r.content)
z = zipfile.ZipFile(s, "r")
d = {}
for i in z.infolist():
  d[i.filename] = i.comment
#  sys.stdout.write(i.comment)
while True:
  filename = '%s.txt' % nothing
  f = z.open(filename)
  t = f.read()
#  print t
  sys.stdout.write(d[filename])
  m = pat.search(t)
  if m:
    nothing = int(m.groups()[0])
#    print 'Next: %d' % nothing
  else:
#    print t
    break
