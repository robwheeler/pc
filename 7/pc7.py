#!/usr/bin/env python

"""
http://www.pythonchallenge.com/pc/def/oxygen.html
"""

import requests
import StringIO
from PIL import Image
import sys

r = requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png')
s = StringIO.StringIO(r.content)
i = Image.open(s)
width, height = i.size
y = height / 2
for x in xrange(0, width, 7):
  p = i.getpixel((x, y))
  sys.stderr.write(chr(p[0]))

print
l = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print "".join(chr(x) for x in l)
    
