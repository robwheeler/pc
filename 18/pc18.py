#!/usr/bin/env python

"""
http://www.pythonchallenge.com/pc/return/balloons.html
"""

import requests
import gzip
from StringIO import StringIO
from PIL import Image
import difflib
from collections import defaultdict

r = requests.get('http://www.pythonchallenge.com/pc/return/deltas.gz', auth = ('huge', 'file'))
left, right = [], []
for line in gzip.GzipFile(fileobj=StringIO(r.content)).readlines():
  left.append(line[:53])
  right.append(line[54:].strip())

d = defaultdict(list)
for line in difflib.ndiff(left, right):
  d[line[0]].extend((x.decode('hex') for x in line[1:].split()))

for key in d.keys():
  im = Image.open(StringIO(''.join(d[key])))
  im.show()
