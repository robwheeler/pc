#!/bin/bash
egrep  '[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]' ./pc3.py  | sed -r -e 's/.*[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z].*/\1/'
