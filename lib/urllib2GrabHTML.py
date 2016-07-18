#!/usr/bin/python

import urllib2
import time
import StringIO
import re
import sys

def textToDict(content):
	diction = dict()
	buf = StringIO.StringIO( content )#do str as file
	
	for line in buf:
		#print line
		if not (re.match(r'^\s*[0-9]*$', line)) :
			singleLine=line.split(':', 1)
			second = re.sub('[\[\]\'\"]', '', singleLine[1].rstrip("\n").rstrip(",")) #remove [ ] ' "
			
			firstaskey = singleLine[0].rstrip().lstrip()
			if('product_' in firstaskey):
				#print firstaskey, second
				diction[ firstaskey] = float(second) if second.replace('.','',1).isdigit() else second.rstrip().lstrip()
	buf.close()

	return diction

	
##withdraw info from newegg
def getUTAG(item = 'N82E16834231495R'):
	#print "checking ", item		
	sys.stdout.write('\r'+"checking " + item)
	
	ts=time.time()
	sys.stdout.write(".")
	url = 'http://www.newegg.com/Product/Product.aspx'
	req = urllib2.Request(url+'?Item='+str(item))
	sys.stdout.write(".")
	req.add_header('User-Agent','Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')## pretend I am using firefox
	sys.stdout.write(".")
	response = urllib2.urlopen(req)## get the whole html
	sys.stdout.write(".")
	
	the_page = response.read()
	sys.stdout.write(".")
	response.close()
	sys.stdout.write(".")
	first_index=the_page.find('utag_data')
	
	first_data=the_page.find('{', first_index)+1
	last_data=the_page.find('}', first_data)	
	#print "getUTAG: ", item, " ", time.time()-ts
	sys.stdout.write('\r' + "getUTAG "+ item+ " using "+ str(time.time()-ts)+" Sec\n")
	
	return the_page[first_data:last_data]