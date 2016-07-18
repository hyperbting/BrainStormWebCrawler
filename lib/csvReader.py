#!/usr/bin/python
import sys
import csv
import os.path
import time

def loadcsv(csvfilepath='csv/newegg.csv', takeColumn = 1):
	with open( csvfilepath, 'r') as csvfile:
		rlist=list()
		try:
			f = csv.reader(csvfile)
			rlist = list(f)
		finally:
			csvfile.close()
			
		for i in range(0,len(rlist)):
			if takeColumn==1:
				rlist[i]=rlist[i][0]
			else:
				rlist[i]=rlist[i][:takeColumn]
		return rlist# return item_id in list ["n123","n456"]

def savecsv(content, csvfilepath='result/'+time.strftime("%Y%m%d %H-%M-%S")+'_result.csv'):
	#if not os.path.isfile(csvfilepath):
		
	with open( csvfilepath, 'wb') as csvfile:
		f = csv.writer(csvfile, delimiter=',')
		f.writerows(content)
	return csvfilepath
		
