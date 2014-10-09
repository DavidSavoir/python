#!/usr/bin/env python3
import time, os, winsound

print("Content-Type: text/html\n\n")  # html markup follows

timeStr = time.strftime("%c") # obtains current time

htmlFormat = """
<html>
  <Title>The Time Now</Title>
<body>
  <p>The current Central date and time is:  {timeStr}</p>
</body>
</html> """

print(htmlFormat.format(**locals())) # see embedded %s ^ above

"""

def main():
    Timerreason1=input("Enter customer: ")
    minutes = float(input("Input minutes : "))
    os.system('CLS')
    counter=minutes*60
    mins=int(counter/60)
    hr=int(mins/60)
    while counter > 0:
        os.system('CLS')
        counter-=1
        hr, sc = divmod(counter, 3600)
        mn, sc = divmod(sc, 60)
        print ("########################################")
        print("")
        print ("Countdown for task %s"%Timerreason1)
        print ("  %d hours, %d minutes and %d seconds" % (hr, mn, sc))
        print("")
        print ("########################################")
        mins=int(counter/60)
        hr=int(mins/60)
        time.sleep(1)
    else:
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
        #winsound.MessageBeep([type=MB_ICONEXCLAMATION])
        #winsound.MessageBeep([type=MB_ICONEXCLAMATION])
        #winsound.MessageBeep([type=MB_ICONEXCLAMATION])
        #winsound.MessageBeep([type=MB_ICONEXCLAMATION])
        #winsound.MessageBeep([type=MB_ICONEXCLAMATION])
        winsound.Beep(Freq,Dur)
        time.sleep(1)
        winsound.Beep(Freq,Dur)
        time.sleep(1)
        winsound.Beep(Freq,Dur)
        print("")
main()
"""