import os

files = os.listdir(".")

files.sort()


for f in files:
	if f.startswith("CHI_eCom_"):	
		os.rename(f, f[23:])


