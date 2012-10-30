#!/usr/bin/env python

"""
http://www.pythonchallenge.com/pc/return/evil.html
"""

import requests
import StringIO
from PIL import Image, ImageDraw

r = requests.get('http://www.pythonchallenge.com/pc/return/evil2.gfx', auth=('huge', 'file'))
for i in xrange(5):
  s = r.content[i::5]
  try:
    im = Image.open(StringIO.StringIO(s))
    im.show()
  except:
    pass

