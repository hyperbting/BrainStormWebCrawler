#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

with sqlite3.connect('records.db') as con:
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data
	
def readFromSQLite3(content):
	##ts=time.time()
	diction = dict()
	buf = StringIO.StringIO( content )#do str as file
	
	for line in buf:
		print line
		if not (re.match(r'^\s*[0-9]*$', line)) :
			singleLine=line.split(':', 1)
			second = re.sub('[\[\]\'\"]', '', singleLine[1].rstrip("\n").rstrip(",")) #remove [ ] ' "
			
			firstaskey = singleLine[0].rstrip().lstrip()
			if('product_' in firstaskey):
				print firstaskey, second
				diction[ firstaskey] = float(second) if second.replace('.','',1).isdigit() else second.rstrip().lstrip()
	buf.close()
	
	##ts = time.time()-ts
	##print "textToDict: ", ts
	##print diction
	return diction
	
conn = sqlite3.connect('example.db')

def main():
    print 'main'
	
if __name__ == "__main__":
	main()