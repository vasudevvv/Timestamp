# TIMESTAMP Screenshot V.5 (FINAL)
#
# A Timestamp Programme with auto executes at the startup of OS and runs until shutdown and meanwhile changes names of any screenshot taken by the current date
# If a screenshot(Image) already exists with the current timestamp, then the new image will be saved as ("DATE"+ "("+ No. of preexiting screenshots with the same date +")")
# V.5 enables drive upload failsafe, i.e if for some reason the timestamps are not uploaded to the drive, then they will be reuploaded automatically
#     as soon as net connectivity is available
# V.5 also enables the program to execute even if the screenshot is not uploaded (which previously used to crash upon failiure in upload), this enables the 
# 	  program to work in the background without any interruptions and until the system is powered off

import fnmatch                                                            # Fnmatch enables us to use SQL like, wildcard searches in strings 
import os
import datetime
from PIL import Image
import time

# Python API's for authentication and data access/modification, for googledrive
from pydrive.drive import GoogleDrive                                    
from pydrive.auth import GoogleAuth

# This function enables lookup at the contents of a specific text file, which contains the names of the timestamp'd screenshots that were not
# uploaded to the drive and upon finding one, will try to upload it to the Google drive in the background
def UNUPLOADABLE_UPLOADER():
     
	# Path variable stores the path where the timestamp was located if it is encountered
	path = ""
	ti = 0
	
	# Checks whether the UNUPLOADABLE_SCREENSHOTS.txt (txt file which stores the names of the unuploadable screenshots) file exists 
	if os.path.isfile("C:\\Users\\Glock\\Pictures\\Screenshots\\UNUPLOADABLE_SCREENSHOTS.txt"):
		file = open("C:\\Users\\Glock\\Pictures\\Screenshots\\UNUPLOADABLE_SCREENSHOTS.txt",'r')
		
		# A loop which goes through each line of the txt file and stores the content of that line in the variable- line
		for line in file:
		
			# This if condition is true if the eof() is encountered
			if line == "":
				break
			
			# This line ensures that the file is a timestamp'd file and hence matches its syntax
			elif fnmatch.fnmatch(line, "*-*-*.png\n"):
			
				# Getting the date, month and year of the timestamp screenshot
				d, m, y = line.split("-")
				y = y[0:4:]
				month_folder = m + "-" + y
				date_folder = d + "-" + m + "-" + y
				
				# Removes \n from the end of the timestamp file name which by default is like (timestamp_name + "\n")
				line = line[:-1:]
				
				# These two condition are exclusive of each other, and provide a value to the path variable if the filename actually exists
				if os.path.isfile('C:\\Users\\Glock\\Pictures\\Screenshots\\OLD SCREENSHOTS\\' + month_folder + '\\' + date_folder + "\\" + line):
					path = 'C:\\Users\\Glock\\Pictures\\Screenshots\\OLD SCREENSHOTS\\' + month_folder + '\\' + date_folder + "\\" + line
			
				elif os.path.isfile('C:\\Users\\Glock\\Pictures\\Screenshots\\' + line):
					path = 'C:\\Users\\Glock\\Pictures\\Screenshots\\' + line
				
				# This condition is true if the file exists in one of the provided locations
				if not path == "":
				
						# The try block is complete if the screenshot successfully gets uploaded to the drive, and its entry is removed
						# from the UNUPLOADABLE_SCREENSHOTS.txt file
						try:
							f = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": fid}]})
							f.SetContentFile(path)
							f['title'] = line
							f.Upload()
							path = ""
							
							# Storing the contents of the UNUPLOADABLE_SCREENSHOTS.txt, in a variable (buff)
							file_write = open("C:\\Users\\Glock\\Pictures\\Screenshots\\UNUPLOADABLE_SCREENSHOTS.txt",'r')	
							buff = file_write.read()
							file_write.close()
							
							line = line + "\n"
							
							# Removing the line which contains the currently uploaded screenshot name, from the UNUPLOADABLE_SCREENSHOTS.txt file
							file_write = open("C:\\Users\\Glock\\Pictures\\Screenshots\\UNUPLOADABLE_SCREENSHOTS.txt",'w')
							# This statement removes the entry of the uploaded timestamp'd file from the UNUPLOADABLE_SCREENSHOTS.txt
							file_write.write(buff.strip(line)+"\n")
							
							file_write.close()
							
						
						# If the above is not true it continues to check the other entries in the file
						except:
							continue
		file.close()


# client_secrets.json is a file which contains our googledrive account credentials
# settings.yaml is a file which contains OAuth credentials of our googledrive account which allows background offline authentication of googledrive account
# which by default requires Webbrowser or commandline authentication 
# By default both the files (settings.yaml and client_secrets.json) should be located in the same directory as our python program
gauth = GoogleAuth("settings.yaml")
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
fid = 'FOLDER_ID'                  # fid (file id) is a unique id of the googledrive folder in which we want to upload our files to

i = 0
k = ""
date = str(datetime.date.today().day) + "-" + str(datetime.date.today().month) + "-" + str(datetime.date.today().year) 

# This function gets called once, and upon its execution checks whether there are unuploaded screenshots or not
# If they exists then tries to upload them to the specified google drive account
UNUPLOADABLE_UPLOADER()	  

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
			# Try except to enable the execution of the program even if the upload fails for some reason
			try:
				f = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": fid}]})
				f.SetContentFile("C:\\Users\\Glock\\Pictures\\Screenshots\\" + date + k + ".png")
				f['title'] = date + k + ".png"
				f.Upload()
				k = ""
				i = 0
			
			# This except block prevents the termination of the program, if the screenshot taken is not uploaded to the google drive
			# If the screenshot could not be uploaded, then then entry of the unuploaded screenshot gets added in the UNUPLOADABLE_SCREENSHOTS.txt
			# file. This file contains the name of all the screenshots which were not uploaded
			except:
			
				# This conditon checks whether the UNUPLOADABLE_SCREENSHOTS.txt file exists or not
				if not os.path.isfile("C:\\Users\\Glock\\Pictures\\Screenshots\\UNUPLOADABLE_SCREENSHOTS.txt"):
					file = open("C:\\Users\\Glock\\Pictures\\Screenshots\\UNUPLOADABLE_SCREENSHOTS.txt",'w+')
					file.write("THIS FILE CONTAINS THE NAME OF ALL THE TIMESTAMP SCREENSHOTS THAT DIDN'T GOT UPLOADED TO THE GOOGLE DRIVE\n")
					file.write("YOU CAN MANUALLY UPLOAD THE BELOW MENTIONED FILES TO GOOGLE DRIVE \n\n")
					file.write("################################################################################################\n\n\n\n")
					file.close()
					
				# This snippet of code adds the entry of the unuploaded screenshot in the UNUPLOADABLE_SCREENSHOTS.txt file
				log = open("C:\\Users\\Glock\\Pictures\\Screenshots\\UNUPLOADABLE_SCREENSHOTS.txt",'a')
				log.write(date + k + ".png\n")
				log.close()
				k = ""
				i = 0
				
			

   
