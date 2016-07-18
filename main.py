#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os 
import time

sys.path.append(os.getcwd()) 
sys.path.append(os.getcwd()+'/lib') 
import urllib2GrabHTML
import csvReader

	
def main():
	
	mySettingDict = dict()
	###loading setting###
	for singleSetting in csvReader.loadcsv('csv/settings.csv', 2):
		mySettingDict[singleSetting[0]]=singleSetting[1]
	
	while True:
		ts=time.time()
		listotcsv = list()
		listotcsv.append( [ 'id', 'price', 'inStock', 'title' ] );
		
		for singleid in csvReader.loadcsv():
			
			result = urllib2GrabHTML.textToDict(urllib2GrabHTML.getUTAG(singleid ) )
			
			if "product_sale_price" in result:##case in stock
				listotcsv.append( [ singleid , result['product_sale_price'], result['product_instock'], result['product_title'] ] );
			elif "product_unit_price" in result: ## not in stock	
					listotcsv.append( [singleid , result['product_unit_price'], result['product_instock'], result['product_title'] ])
			else:
				listotcsv.append( [singleid , 'UnKnOwN id' ])
			
			#last line of for loop...delay for 2 second!
			takeNap( int(mySettingDict["delayEachEntry"]) )
				
		rfilepath=csvReader.savecsv(listotcsv, 'result/'+str(time.strftime("%Y%m%d %H-%M-%S"))+'_result.csv')
		print "\nmain: ", str(time.time()-ts), " check "+rfilepath+" for result"
		takeNap( int(mySettingDict['delayEachRound']) )
	###os.system("pause")

def takeNap(second):
	for x in range (0, second):
			delaysecond = second-x
			b = ("sleeping" + "." * x+ "("+str(delaysecond))####+") or press Shift-X to stop!")
			sys.stdout.write('\r'+b)
			time.sleep(1)
	cleanNreturn()
	
def cleanNreturn(space=50):
	b = (" " * space)
	sys.stdout.write('\r'+b)
	sys.stdout.write('\r')
			
if __name__ == "__main__":
	main()