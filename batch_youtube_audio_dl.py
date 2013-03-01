#!/usr/bin/env python
import sys
import subprocess

filename = sys.argv[1] #containing multiple video links, one per line
#options = "-t -f 37"
op1 = "-t"
op2 = "--extract-audio"
op3 = "--audio-format"
op4 = "mp3"
op5 = "--keep-video"
op14 = "-t --max-quality --extract-audio --audio-format mp3 --keepvideo"
scriptname = "./youtube-dl" #script from http://rg3.github.com/youtube-dl/

#print filename
#with open(filename) as f:
#    content = f.readlines()
lines = [line.strip() for line in open(filename)]

for line in lines:
    print "Getting: " + line
    subprocess.call([scriptname, line, op1, op2, op3, op4, op5]) #22 or 84 is MP4 at 720 - see https://en.wikipedia.org/wiki/YouTube#Quality_and_codecs