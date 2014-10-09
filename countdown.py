import os,time,winsound
Timerreason1=input("Enter customer: ")
Timerduration1=int(input("Escallation time in minutes: "))
if Timerduration1 < 61: 
	hours=0
	minutes=Timerduration1
	sec=0
	counter=hours*3600+minutes*60+sec
	mins=int(counter/60)
	hr=int(mins/60)
while counter > 0:
    counter-=1
    hr, sc = divmod(counter, 3600)
    mn, sc = divmod(sc, 60)
    print (Timerreason1)
    print ('%d minutes and %d seconds' % ( mn, sc))
    os.system('CLS')
    mins=int(counter/60)
    hr=int(mins/60)
    time.sleep(1)
Freq = 1000 # Set Frequency To 2500 Hertz
Dur = 1000 # Set Duration To 1000 ms == 1 second
print ("Take action for %s" % Timerreason1)
winsound.Beep(Freq,Dur)
time.sleep(1)
winsound.Beep(Freq,Dur)
time.sleep(1)
winsound.Beep(Freq,Dur)
