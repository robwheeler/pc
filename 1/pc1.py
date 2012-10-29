#!/usr/bin/env python

"""
    http://www.pythonchallenge.com/pc/def/map.html
"""

import string

clue = """
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""

url = 'map'

def trans(s):
  return string.translate(s, string.maketrans(string.letters[:26], string.letters[2:26]+string.letters[:2]))

print trans(clue)
print 'http://www.pythonchallenge.com/pc/dev/%s.html' % trans(url)
