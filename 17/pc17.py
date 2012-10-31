#!/usr/bin/env python

"""
http://www.pythonchallenge.com/pc/def/romance.html
"""

import re
import requests
import bz2
import urllib


url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s'
nothing = 12345
pat = re.compile('next busynothing is ([0-9]*)')
cookies = []
while True:
  r = requests.get(url % nothing)
  cookies.append(r.cookies['info'])
  m = pat.search(r.content)
  if m:
    nothing = int(m.groups()[0])
  else:
    break

print bz2.decompress(urllib.unquote_plus("".join(cookies)))

# is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.

# Mozart's father is Leopold, so go back and lookup his phone number


import xmlrpclib
r = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')
print r.phone('Leopold')

# Leopold's number is 555-VIOLIN
r = requests.get('http://www.pythonchallenge.com/pc/stuff/violin.php', cookies={'info': urllib.quote_plus('the flowers are on their way')})
print r.content
