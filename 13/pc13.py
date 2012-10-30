#!/usr/bin/env python

"""
http://www.pythonchallenge.com/pc/return/disproportional.html
"""

import xmlrpclib

r = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')
print r.phone('Bert')
