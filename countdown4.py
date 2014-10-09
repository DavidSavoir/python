import time, os, winsound
def main(*args):
    if SnoozeQ ==False:
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
            print("")
            SnoozeQuestion = input ("Would you like to snooze ? Y/N ")
            if SnoozeQuestion == "Y" or SnoozeQuestion == 'y':
                SnoozeDuration = input ("How many more minutes do you want to snooze ?")
                main(SnoozeQuestion, SnoozeDuration)


main()