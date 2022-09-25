import json
import os 
import sys


fname = 'dictionary.json'
if not os.path.isfile(fname):
	print("File does not exist")
	sys.exit()
f = open(fname)

data = json.load(f)

name = input("Enter a word: ")
while name != '':
	if name.lower() in data.keys():
		print("%s = '%s'" % (name, data[name.lower()]))
	else:
		print(name, " is not present")
	print("")
	name = input("Enter a word: ")

f.close
