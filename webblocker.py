import os , time , sys
from datetime import datetime

websites = ['www.xvideos.com' , 'www.xnxx.com' , 'www.pornhub.com' , 'www.youporn.com' , 'www.bangbros.com' ]
redirect = '127.0.0.1'
os.chdir("C:\\Windows\\System32\\drivers\\etc")
filename = "C:\\Windows\\System32\\drivers\\etc\\hosts"

while True:
	file = open(filename , 'r+')
	content = file.read()
	for i in websites:
		if i in content:
			pass
		else:
			file.write('\n' + redirect + ' ' + i)
	file.close()
	time.sleep(20)