#!/usr/bin/env python3

#Civ Ysh K (2016) GPLv3

import sys

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: %s subtitle.vtt" % (sys.argv[0]))
		sys.exit(0)
		
	originName = sys.argv[1]
	if originName[-4:] != ".vtt":
		print("Usage: %s subtitle.vtt" % (sys.argv[0]))
		sys.exit(0)
	
	destinyName = originName[:-4] + ".srt"
	with open(originName, "r") as origin:
		with open(destinyName, "w") as destiny:
			print("Converting %s to %s" % (originName, destinyName))
			for line in origin.readlines():
				#Be careful. This doesn't check if this line is a timecode line
				#or a text line. But hey I don't have all night.
				#If original vtt file doesn't have numbering before timecodes,
				#the resulting srt won't have either, and thus it won't work.
				line.replace("WEBVTT", "")
				if line.find(" --> ") != -1:
					line = line.replace(".", ",")
				destiny.write(line)
				
