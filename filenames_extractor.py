import os
import re
import datetime
#import csv

from pathlib import Path

cur_path = Path.cwd()

current_day = datetime.date.today()

today = datetime.date.strftime(current_day, "%m/%d/%Y")

files = os.listdir(cur_path)

files.sort()

temp_file = open("filenames_colorcode.csv", "w")

temp_file.write("File Name" + "," + "Article Number" + "," +  "Color Code" + "," +  "Date Asset Delivered" +  "\n")

for f in files:
	
	temp = []
	if f.__contains__('.jpg') or f.__contains__( '.gif'): 
			
		#temp = re.split(r"[-_;,.\s]\s*", f)  '''to split any underscorehyphen, and other separator'''
		temp_file.write(f + "," + f[:9] + "," + f[9:-4] + "," + today + "\n" )
		#temp_file.write(",".join(temp[:-1]))
		#temp_file.write("\n")

temp_file.close()
