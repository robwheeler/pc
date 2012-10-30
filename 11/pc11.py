#!/usr/bin/env python

"""
http://www.pythonchallenge.com/pc/def/oxygen.html
"""

import requests
import StringIO
from PIL import Image, ImageDraw

r = requests.get('http://www.pythonchallenge.com/pc/return/cave.jpg', auth=('huge', 'file'))
s = StringIO.StringIO(r.content)
src = Image.open(s)
dst1 = Image.new("RGB", (src.size[0]/2, src.size[1]/2))
d1 = ImageDraw.Draw(dst1)
dst2 = Image.new("RGB", (src.size[0]/2, src.size[1]/2))
d2 = ImageDraw.Draw(dst2)
width, height = src.size
for y in xrange(height):
  for x in xrange(width):
    p = src.getpixel((x, y))
    if (x ^ y) & 1 == 1:
      d1.point((x/2, y/2), p)
    else:
      d2.point((x/2, y/2), p)
dst1.show()
dst2.show()
