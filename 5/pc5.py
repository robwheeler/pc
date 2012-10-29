#!/usr/bin/env python

"""
http://www.pythonchallenge.com/pc/def/peak.html
"""

import requests
import pickle
import sys

r = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')
list_of_lists = pickle.loads(r.content)
for list_of_tuples in list_of_lists:
  for c, n in list_of_tuples:
    sys.stdout.write(c*n)
  sys.stdout.write('\n')
