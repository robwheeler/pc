#!/usr/bin/env python

"""
http://butter:fly@www.pythonchallenge.com/pc/hex/copper.html
"""

import requests
from PIL import Image, ImageDraw
from StringIO import StringIO

r = requests.get('http://www.pythonchallenge.com/pc/hex/white.gif', auth = ('butter', 'fly'))

im = Image.open(StringIO(r.content))
dst = Image.new("RGB", (250, 250))
draw = ImageDraw.Draw(dst)

points = [10, 10]
for frame in xrange(133):
  im.seek(frame)
  frame += 1
  i = list(im.getdata()).index(8)
  if i == 100 * 200 + 100:
    draw.line(points, fill=(255, 255, 255))
    points = [points[0] + 30, points[1]]
  else:
    points.append(points[-2] + (i % im.size[0] - 100))
    points.append(points[-2] + (i / im.size[0] - 100))

draw.line(points, fill=(255, 255, 255))
dst.show()

