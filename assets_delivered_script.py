import os
import re
import datetime
from pathlib import Path
from xlwt import *

cur_path = Path.cwd()

current_day = datetime.date.today()

today = datetime.date.strftime(current_day, "%m/%d/%Y")

today_in_file_name = datetime.date.strftime(current_day, "%m_%d_%Y")

files = os.listdir(cur_path)

files.sort()

workbook = Workbook(encoding = 'utf-8')

table = workbook.add_sheet('Delivered_Assets')

table.write(0, 0, 'Filename')

table.write(0, 1, 'Style Number')

table.write(0, 2, 'Color Code')

table.write(0, 3, 'Date Asset Delivered')

line = 1

for f in files:
	
	temp = []
	if f.__contains__('.jpg') or f.__contains__( '.gif'): 
			
		table.write(line, 0, f)

		table.write(line, 1, f[:9])

		table.write(line, 2, f[9:-4])

		table.write(line, 3, today)

		line += 1

workbook.save('Delivered_Asset_' + today_in_file_name + '.xls')
