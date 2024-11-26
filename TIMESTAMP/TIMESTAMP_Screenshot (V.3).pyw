# TIMESTAMP Screenshot (V.3)
#
# A Timestamp Programme with auto executes at the startup of OS and runs until shutdown and meanwhile changes names of any screenshot taken by the current date
# If a screenshot(Image) already exists with the current timestamp, then the new image will be saved as DATE + ( + No. of preexiting screenshots with the same date + ) 
# V.3 adds new featurs such as sorting screenshots according to their months and dates in their respective folders, now there will be 1 folder for each day and 1 for each month
# (the date folders will be in their respective month folders) 
# Now only today's screenshots will be in the screenshot folder, and the older screenshots will moved to their month/date folders at every system startup

import fnmatch                                                            # Fnmatch enables us to use SQL like, wildcard searches in strings 
import os
import datetime
from PIL import Image
import time

i = 0
k = ""
date = str(datetime.date.today().day) + "-" + str(datetime.date.today().month) + "-" + str(datetime.date.today().year)

# This loop executes ( for once ) at every system startup and does a lookup for old Screenshots in the default Screenshot folder, and moves them
# to their month/date folders

for file in os.listdir('C:\\Users\\Glock\\Pictures\\Screenshots\\'): 

    # Some Conditions to ensure that we are dealing with Sorting of Timestamp'd screenshots and not any other file/folder       
	if not fnmatch.fnmatch(file, date + "*.png"):                        
		if os.path.isdir('C:\\Users\\Glock\\Pictures\\Screenshots\\' + file) or not fnmatch.fnmatch(file, '*-*-*.png'):
			continue
			
		# Getting date, month and year of the TIMESTAMP'd file to create repective Month/Date Folders
		d, m, y = file.split("-")
		y = y[0:4:]
		month_folder = m + "-" + y
		date_folder = d + "-" + m + "-" + y
		image = Image.open("C:\\Users\\Glock\\Pictures\\Screenshots\\" + file)
		
		# Some Conditions which ensure that month and date folders exists for the current Timestamp'd screenshot
		if not os.path.exists('C:\\Users\\Glock\\Pictures\\Screenshots\\OLD SCREENSHOTS\\'):
			os.makedirs('C:\\Users\\Glock\\Pictures\\Screenshots\\OLD SCREENSHOTS\\')   
		if not os.path.exists('C:\\Users\\Glock\\Pictures\\Screenshots\\OLD SCREENSHOTS\\' + month_folder):
			os.makedirs('C:\\Users\\Glock\\Pictures\\Screenshots\\OLD SCREENSHOTS\\' + month_folder)   
		if not os.path.exists('C:\\Users\\Glock\\Pictures\\Screenshots\\OLD SCREENSHOTS\\' + month_folder +"\\" + date_folder):
			os.makedirs('C:\\Users\\Glock\\Pictures\\Screenshots\\OLD SCREENSHOTS\\' + month_folder + "\\" + date_folder)
			
		image.save('C:\\Users\\Glock\\Pictures\\Screenshots\\OLD SCREENSHOTS\\' + month_folder + '\\' + date_folder + "\\" + file)      
		os.remove('C:\\Users\\Glock\\Pictures\\Screenshots\\' + file)	 
i = 0
k = ""

# This loop executes until the system is turned off (shutdown)
while 1:                                                                          
	time.sleep(5)                                                           # 5 second latency between lookups for new content in the folder
	for file in os.listdir(r'C:\Users\Glock\Pictures\Screenshots'):          
		if fnmatch.fnmatch(file, 'Screenshot*.png'):
			date = str(datetime.date.today().day) + "-" + str(datetime.date.today().month) + "-" + str(datetime.date.today().year) 
			Screenshot = Image.open("C:\\Users\\Glock\\Pictures\\Screenshots\\" + file)
			
			while 1:
			   try:
				   f = open("C:\\Users\\Glock\\Pictures\\Screenshots\\" + date + k + ".png")
				   f.close()
				   i += 1
				   k = "(" + str(i) + ")"
			   except:
				   Screenshot.save("C:\\Users\\Glock\\Pictures\\Screenshots\\" + date + k + ".png")

				   break
			os.remove("C:\\Users\\Glock\\Pictures\\Screenshots\\" + file)