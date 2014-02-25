import time
from Tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(time.strftime( '%I:%M %Y/%m/%d' ))
print(time.strftime( '%I:%M %Y/%m/%d' ))
r.destroy()

# for windows only
import SendKeys
SendKeys.SendKeys("^v")
SendKeys.SendKeys("\r\n")