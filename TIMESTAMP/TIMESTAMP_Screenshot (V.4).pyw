# TIMESTAMP Screenshot V.4 
#
# A Timestamp Programme with auto executes at the startup of OS and runs until shutdown and meanwhile changes names of any screenshot taken by the current date
# If a screenshot(Image) already exists with the current timestamp, then the new image will be saved as ("DATE"+ "("+ No. of preexiting screenshots with the same date +")")
# V.4 adds Sync to GoogleDrive, i.e new Timestamp'd screenshots will be automatically uploaded to a Folder in the provided GoogleDrive account
# This ensures data redundancy on the cloud, i.e if local copy of the screenshots is somehow deleted then its copy can be easily retrieved from googledrive
# 1 screenshots = ~200kb in size, and googledrive provides us with 15Gb of free storage, so we won't run in storage issue anytime sooner then 10 yrs

import fnmatch                                                            # Fnmatch enables us to use SQL like, wildcard searches in strings 
import os
import datetime
from PIL import Image
import time

# Python API's for authentication and data access/modification, for googledrive
from pydrive.drive import GoogleDrive                                    
from pydrive.auth import GoogleAuth

# client_secrets.json is a file which contains our googledrive account credentials
# settings.yaml is a file which contains OAuth credentials of our googledrive account which allows background/offline authentication of googledrive account
# which by default requires Webbrowser or commandline authentication 
# By default both the files (settings.yaml and client_secrets.json) should be located in the same directory as our python program
gauth = GoogleAuth("settings.yaml")
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
fid = 'FOLDER_ID'                  # fid (file id) is a unique id of the googledrive folder in which we want to upload our files to

i = 0
k = ""
date = str(datetime.date.today().day) + "-" + str(datetime.date.today().month) + "-" + str(datetime.date.today().year)   

for file in os.listdir('C:\\Users\\Glock\\Pictures\\Screenshots\\'):     
	if not fnmatch.fnmatch(file, date + "*.png"):                        
		if os.path.isdir('C:\\Users\\Glock\\Pictures\\Screenshots\\' + file) or not fnmatch.fnmatch(file, '*-*-*.png'):
			continue
		d, m, y = file.split("-")
		y = y[0:4:]
		month_folder = m + "-" + y
		date_folder = d + "-" + m + "-" + y
		image = Image.open("C:\\Users\\Glock\\Pictures\\Screenshots\\" + file)
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
		   
			# This snippet creates a copy of current TIMESTAMP'd screenshot, in the provided google drive folder
			f = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": fid}]})
			f.SetContentFile("C:\\Users\\Glock\\Pictures\\Screenshots\\" + date + k + ".png")
			f['title'] = date + k + ".png"
			f.Upload()

   
