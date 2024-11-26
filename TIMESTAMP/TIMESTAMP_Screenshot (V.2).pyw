# TIMESTAMP Screenshot (V.2)
#
# A Timestamp Program with executes at the startup of OS and runs until shutdown and meanwhile changes names of any screenshot taken by the current date
# If a screenshot(Image) already exists with the current timestamp, then the new image will be saved as, DATE + ( + No. of preexiting screenshots with the same date + )
# V.2 enables working on the Screenshot's Folder, i.e a screenshot taken using std screenshot key (WIN + PrtScn) will also be TIMESTAMP'd


import fnmatch                                                                # Fnmatch enables us to use SQL like wildcard searches in strings
import os
import datetime
from PIL import Image
import time

i = 0
k = ""
date = str(datetime.date.today().day) + "-" + str(datetime.date.today().month) + "-" + str(datetime.date.today().year) 
 
# This loop executes until the system is turned off (shutdown)
while 1:                                                                          
	time.sleep(5)                                                           # 5 second latency between lookups for new content in the folder
	for file in os.listdir(r'C:\Users\Glock\Pictures\Screenshots'):
    # File is a variable which stores names of the files/folders in the specified directory
	
		if fnmatch.fnmatch(file, 'Screenshot*.png'):
		# This Condition only allows file which match the screenshot syntax (Screenshot *.png), excluding other files/folders in the directory
		
			date = str(datetime.date.today().day) + "-" + str(datetime.date.today().month) + "-" + str(datetime.date.today().year) 
			Screenshot = Image.open("C:\\Users\\Glock\\Pictures\\Screenshots\\" + file)
			
			# This loop does the naming of the screenshot taken according to the previous screenshots in the directory
			while 1:
			   try:
				   f = open("C:\\Users\\Glock\\Pictures\\Screenshots\\" + date + k + ".png")
				   f.close()
				   i += 1
				   k = "(" + str(i) + ")"
			   except:
				   Screenshot.save("C:\\Users\\Glock\\Pictures\\Screenshots\\" + date + k + ".png")
				   break
				   
		    # Removing the old Screenshot file after its Timestamp'd version is created
			os.remove("C:\\Users\\Glock\\Pictures\\Screenshots\\" + file)