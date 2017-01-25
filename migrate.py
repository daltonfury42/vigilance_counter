#!/bin/env python3

"""
Program to migrate data from old vigilance program to the new program. Usage: pytho3 manage.py shell < migrate.py

"""


import ast
import re
from circulation.models import CheckOuts
from datetime import datetime
import vigilance_counter


fp = open("vigilance_backup.sql", "r")
sqlFile = fp.read()
fp.close()

insertCommands = sqlFile.split(';')[17:20]

for command in insertCommands:
	for entry in re.findall(r'\([^)]*\)', command):
		data = ast.literal_eval(entry)
		print(data)
		CheckOuts(roll=data[0], accn_no=data[1], time_stamp=datetime.strptime(data[2], "%Y-%m-%d %H:%M:%S")).save()
		

