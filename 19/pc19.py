#!/usr/bin/env python

"""
http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html
"""

import requests
import email
from StringIO import StringIO

r = requests.get('http://www.pythonchallenge.com/pc/hex/bin.html', auth = ('butter', 'fly'))

body = r.content
body = body[body.index('<!--\n')+5:]
msg = email.message_from_file(StringIO(body))
for part in msg.walk():
  if part.get_content_maintype() == 'multipart':
    continue
  open(part.get_filename(), 'w').write(part.get_payload(decode=True))

import wave
import struct
w = wave.open('indian.wav')
n = wave.open('answer.wav', 'w')
n.setparams(w.getparams())
n.writeframes(struct.pack('>'+'h'*w.getnframes(), *struct.unpack('<'+'h'*w.getnframes(), w.readframes(w.getnframes()))))
n.close()

