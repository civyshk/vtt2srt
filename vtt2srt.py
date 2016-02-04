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
			for line in origin.readlines()[2:]:
				#be careful. This doesn't check if this is a time SRT line
				#or a text line. But hey I don't have all night.
				if line.find(" --> ") != -1:
					line = line.replace(".", ",")
				destiny.write(line)
				
