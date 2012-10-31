#!/usr/bin/env python

"""
http://www.pythonchallenge.com/pc/return/italy.html
"""

import requests
import StringIO
from PIL import Image, ImageDraw

r = requests.get('http://www.pythonchallenge.com/pc/return/wire.png', auth=('huge', 'file'))
src = Image.open(StringIO.StringIO(r.content))
im = Image.new("RGB", (100, 100))
draw = ImageDraw.Draw(im)

min_x, min_y = 0, 0
max_x, max_y = 99, 99
dx, dy = 1, 0
x, y = 0, 0

for i in xrange(100*100):
  draw.point((x, y), fill=src.getpixel((i, 0)))
  x += dx
  y += dy
  if x > max_x:
    dx = 0
    dy = 1
    x = max_x
    y += dy
    min_y += 1
  elif x < min_x:
    dx = 0
    dy = -1
    x = min_x
    y += dy
    max_y -= 1
  if y > max_y:
    dx = -1
    dy = 0
    y = max_y
    x += dx
    max_x -= 1
  elif y < min_y:
    dx = 1
    dy = 0
    y = min_y
    x += dx
    min_x += 1
im.show()
