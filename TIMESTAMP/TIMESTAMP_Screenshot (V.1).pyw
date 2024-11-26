# TIMESTAMP Screenshot (V.1)
#
# a python program which enables us to taken screenshots via python script and then saves them to Screenshot folder, where the name of the screenshot will be the current date
# User has to define a shortcut for execution of this script and should make that shortcut global, i.e if shortcut = 1, the script executes, takes screenshot and renames it 

          
import pyautogui                                        # Python Library for automating mouse and keyboard
import datetime
i = 0

# Getting current date in std form
date = str(datetime.date.today().day) + "-" + str(datetime.date.today().month) + "-" + str(datetime.date.today().year)   
image = pyautogui.screenshot()                          # Takes the screenshot of the display
k = ""

# This loop does a lookup for Pre-Existing Timestamp'd screenshots and arranges the new one's according to the previous ones by numbering them
while 1:                                                
 try:
    f = open("C:\\Users\\Glock\\Pictures\\Screenshots\\" + date + k + ".png")
    f.close()
    i += 1
    k = "(" + str(i) + ")"
 except:
    image.save("C:\\Users\\Glock\\Pictures\\Screenshots\\" + date + k + ".png")
    break
