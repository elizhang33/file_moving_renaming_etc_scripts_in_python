import os
import re


files = os.listdir(".")

files.sort()


for f in files:
	if ".gif" in f:
	
		f1 = re.sub('.jpg', '', f)
	
		f2 = f1.replace('___', '_')

		f3 = re.sub('_[0-9][0-9][0-9]_', '_', f2)

		os.rename(f, f3)


		


