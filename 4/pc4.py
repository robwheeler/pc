#!/usr/bin/env python

"""
http://www.pythonchallenge.com/pc/def/linkedlist.html
"""

import re
import requests


url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
nothing = 12345
pat = re.compile('and the next nothing is ([0-9]*)')

while True:
  r = requests.get(url % nothing)
  print r.content
  m = pat.search(r.content)
  if m:
    nothing = int(m.groups()[0])
  elif r.content.endswith('.html'):
    break
  else:
    nothing = nothing / 2
