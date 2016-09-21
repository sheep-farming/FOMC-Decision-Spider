from datetime import datetime
from time import sleep
import os, urllib, re
altTime = [300,60,30,10]
altTxt = ["5 Minutes", "1 Minutes", "30 Seconds", "10 Seconds"]
altEd = [False, False, False, False]  

timeReleased = datetime(2016,9,22,02,00,00)
isReleased = False
def strr(i):
	if (len(str(i))==1):
		return "0"+str(i)
	return str(i)

while not isReleased:
	nHour = datetime.now().hour
	nMin = datetime.now().minute
	nSec = datetime.now().second
	tOffset = timeReleased - datetime.now()
	tOffset = tOffset.seconds
	print strr(nHour)+":"+strr(nMin)+":"+strr(nSec)+"\t",
	print strr(tOffset/3600) + "H " + strr(tOffset%3600/60) + "M " + strr(tOffset%60) + "S"
	for i in range(len(altTime)):
		if tOffset<=altTime[i]:
			if altEd[i]==False:
				osRetn = os.system("Say -v Daniel FOMC " +altTxt[i])
				print "\t\t**Announcement"
				altEd[i]=True
	if datetime.now()>=timeReleased:
		rawHTML = urllib.urlopen('http://www.federalreserve.gov/newsevents/press/monetary/20160921a1.htm').read()
		r=re.search('(?<=reserve\ balances\ at\ )\d+\.\d*',rawHTML)
		if r:
			print "\n" * 20
			print "FOMC Decision: " + strr(nHour)+":"+strr(nMin)+":"+strr(nSec)+"\t"
			print str(r.group(0))+" Upper Bound"
			print "\n" * 10
			osRetn = os.system("Say -r 250 -v Daniel " +str(r.group(0))+" FOMC Upper Bound")
			osRetn = os.system("Say -r 250 -v Daniel " +str(r.group(0))+" FOMC Upper Bound")
			osRetn = os.system("Say -r 250 -v Daniel " +str(r.group(0))+" FOMC Upper Bound")
			isReleased = True
	sleep(.5)

