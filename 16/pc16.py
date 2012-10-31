#!/usr/bin/env python
"""
http://www.pythonchallenge.com/pc/return/mozart.html
"""

import requests
from StringIO import StringIO
from PIL import Image

r = requests.get('http://www.pythonchallenge.com/pc/return/mozart.gif', auth = ('huge', 'file'))
im = Image.open(StringIO(r.content))
width, height = im.size
for y in xrange(height):
  line = [im.getpixel((x, y)) for x in xrange(width)]
  i = line.index(195)
  line = line[i:] + [0]*i
  [im.putpixel((x, y), p) for x, p in enumerate(line)]
im.show()
