#!/usr/bin/env python

import requests
import re

pat = re.compile('bytes (\d+)-(\d+)/(\d+)')
start = 0
while True:
  r = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', auth = ('butter', 'fly'), headers={'range': 'bytes=%d-' % start})
  if r.status_code == 416:
    break
  if 'content-range' in r.headers:
    m = pat.search(r.headers['content-range'])
    if m:
      print m.groups()
      new = int(m.groups()[1])+1
      if new == start:
        break
      else:
        start = new
      if len(r.content) < 1000:
        print r.content
    else:
      break

end = int(m.groups()[2])
while True:
  r = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', auth = ('butter', 'fly'), headers={'range': 'bytes=%d-%d' % (end-1, end)})
  if r.status_code == 416:
    break
  if 'content-range' in r.headers:
    m = pat.search(r.headers['content-range'])
    if m:
      print m.groups()
      new = int(m.groups()[0])-1
      if new == end:
        break
      else:
        end = new
      if len(r.content) < 1000:
        print r.content
    else:
      break
r = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', auth = ('butter', 'fly'), headers={'range': 'bytes=1152983631-'})

import zipfile
from StringIO import StringIO
z = zipfile.ZipFile(StringIO(r.content))
print z.namelist()
nick = 'invader'
f = z.open('readme.txt', 'r', nick[::-1])
print f.read()

f = z.open('package.pack', 'r', nick[::-1])
pack = f.read()

import zlib
import bz2
d = []
while True:
  did_it = False
  try:
    pack = zlib.decompress(pack)
    d.append('Z')
    did_it = True
  except:
    try:
      pack = bz2.decompress(pack)
      d.append('B')
      did_it = True
    except IOError:
      # neither zlib or bz2 worked, flip data
      pack = pack[::-1]
      print "".join(d)
      d = []
      if len(pack) < 100:
        break

print pack
