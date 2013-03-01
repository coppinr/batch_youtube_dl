#!/usr/bin/env python
import sys
import subprocess

filename = sys.argv[1] #containing multiple video links, one per line
#options = "-t -f 37"
scriptname = "./youtube-dl" #script from http://rg3.github.com/youtube-dl/

#print filename
#with open(filename) as f:
#    content = f.readlines()
lines = [line.strip() for line in open(filename)]

for line in lines:
    print "Getting: " + line
    subprocess.call([scriptname, line, "-t"]) #22 or 84 is MP4 at 720 - see https://en.wikipedia.org/wiki/YouTube#Quality_and_codecs