# TIMESTAMP Screenshot V.6
#
# Built on top of V.5, major performance improvement, User insensitive, allows for precise timestamps (without delay of 5 sec).
# Since V.5 completed all the objectives that i wanted in timestamp, this version (and the later ones) would have a lot more emphasis 
# on improving efficieny of what already has been done. A lot of major/minor changes on different portions of the program has been done. 
# Refer the readme on more info about the changes


import fnmatch
import os
import time
import httplib2

# Python API's for authentication and data access/modification, for googledrive
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

# Userprofile_Env_Var is a variable which stores the location (as a string) obtained by resolving environment variable %userprofile%
# i.e Userprofile_Env_Var = f'C:\\Users\\{UserName}'
Userprofile_Env_Var1 = os.path.expandvars("%userprofile%")
screenshots_path = "\\Pictures\\Screenshots"
pictures_path = Userprofile_Env_Var1 + screenshots_path


def unuploadable_uploader():
    # This function enables lookup at the contents of a specific text file, which contains the names of the timestamp'd screenshots that were not
    # uploaded to the drive and upon finding one, will try to upload it to the Google drive in the background

    # Path variable stores the path where the timestamp was located if it is encountered
    path = ""

    # Checks whether the UNUPLOADABLE_SCREENSHOTS.txt (txt file which stores the names of the unuploadable screenshots) file exists
    if os.path.isfile(f"{pictures_path}\\UNUPLOADABLE_SCREENSHOTS.txt"):
        file = open(f"{pictures_path}\\UNUPLOADABLE_SCREENSHOTS.txt", 'r', encoding='utf-8')

        # A loop which goes through each line of the txt file and stores the content of that line in the variable- line
        for line in file:

            # This if condition is true if the eof() is encountered
            if line == "":
                break

            # This line ensures that the file is a timestamp'd file and hence matches its syntax
            elif fnmatch.fnmatch(line, "*-*-*.png\n"):

                # Getting the date, month and year of the timestamp screenshot
                y, m, d = line.split("-")
                d = d[0:2:]
                month_folder = y + "-" + m
                date_folder = y + "-" + m + "-" + d

                # Removes \n from the end of the timestamp file name which by default is like (timestamp_name + "\n")
                line = line[:-1:]

                # These two condition are exclusive of each other, and provide a value to the path variable if the filename actually exists
                if os.path.isfile(f"{pictures_path}\\OLD SCREENSHOTS\\{month_folder}\\{date_folder}\\{line}"):
                    path = f"{pictures_path}<\\OLD SCREENSHOTS\\{month_folder}\\{date_folder}\\{line}>"

                elif os.path.isfile(f"{pictures_path}\\{line}"):
                    path = f"{pictures_path}\\{line}"

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
                        file_write = open(f"{pictures_path}\\UNUPLOADABLE_SCREENSHOTS.txt", 'r', encoding='utf-8')
                        buff = file_write.read()
                        file_write.close()

                        line = line + "\n"

                        # Removing the line which contains the currently uploaded screenshot name, from the UNUPLOADABLE_SCREENSHOTS.txt file
                        file_write = open(f"{pictures_path}\\UNUPLOADABLE_SCREENSHOTS.txt", 'w', encoding='utf-8')
                        # This statement removes the entry of the uploaded timestamp'd file from the UNUPLOADABLE_SCREENSHOTS.txt
                        file_write.write(buff.strip(line) + "\n")

                        file_write.close()

                    # If the above is not true it continues to check the other entries in the file
                    except:
                        continue

        file.close()


fid = 'FOLDER_ID'

# GoogleDrive Oauth Authentication in try(test) clause to enable safe execution of the program even if the authentication is not successful
try:
    gauth = GoogleAuth("settings.yaml")
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    # This variable is used as a checksum for Gdrive authentication, i.e if authentication is not successful upon program execution variable value = 0
    # if authentication is successful then variable value = 1; if variable value = 0, then the program will try to authenticate itself to GDrive later
    drive_auth = 1

    # Since authentication to Gdrive was succesful, calling the function to upload any files which weren't previously uploaded
    unuploadable_uploader()

# httplib2.ServerNotFoundError error arises if the program could not authenticate the credentials from the server 
except httplib2.ServerNotFoundError:
    drive_auth = 0

date = time.strftime("%Y-%m-%d")

for file in os.listdir(f"{pictures_path}\\"):
    if not fnmatch.fnmatch(file, date + "*.png"):
        if os.path.isdir(f"{pictures_path}\\{file}") or not fnmatch.fnmatch(file, '*-*-*.png'):
            continue

        y, m, d = file.split("-")
        d = d[0:2:]
        month_folder = y + "-" + m
        date_folder = y + "-" + m + "-" + d

        if not os.path.exists(f"{pictures_path}\\OLD SCREENSHOTS\\"):
            os.makedirs(f"{pictures_path}\\OLD SCREENSHOTS\\")
        if not os.path.exists(f"{pictures_path}\\OLD SCREENSHOTS\\{month_folder}"):
            os.makedirs(f"{pictures_path}\\OLD SCREENSHOTS\\{month_folder}")
        if not os.path.exists(f"{pictures_path}\\OLD SCREENSHOTS\\{month_folder}\\{date_folder}"):
            os.makedirs(f"{pictures_path}\\OLD SCREENSHOTS\\{month_folder}\\{date_folder}")

        os.rename(f"{pictures_path}\\{file}",
                  f"{pictures_path}<\\OLD SCREENSHOTS\\{month_folder}\\{date_folder}\\{file}>")

# This loop executes until the system is turned off (shutdown)
while 1:
    time.sleep(5)
    for file in os.listdir(pictures_path):
        if fnmatch.fnmatch(file, 'Screenshot*.png'):
            k = ""
            i = 0

            # Uses the filename, to obtain it's timestamp of creation. Then passes it to strptime to create a time object out of it.
            # then the time object is passed to strftime (with format modifiers) to get desired timestamp string of format
            # (YYYY-MM-DD hh:mm:ss). This string is passed to replace() to replace the ":" with "꞉" (Modified Letter Colon) (reason in readme)
            tstamp_name = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(
                time.ctime(os.path.getctime(pictures_path + "\\" + file)))).replace(":", "꞉")

            while 1:
                try:
                    # Renames the original filename to the timestamp of the file's creation time
                    os.rename(f"{pictures_path}\\{file}", f"{pictures_path}\\{tstamp_name + k + '.png'}")
                    break

                # except will be executed only if a file with the name tstamp_name.png already exists in the directory
                # only reason for this to be true is if another screenshot was taken at the same time as this one.
                # Then the current will be saved as (tstamp_name + "(" + No._of_preexiting_screenshots_with_the_same_tstamp + ")")
                except FileExistsError:
                    i += 1
                    k = f" ({str(i)})"

            # This condition is true, if the OAuth credentials have not been authenticated (failure during OAuth authentication process)
            # The code inside the if: is same as the original OAuth Authentication code
            if drive_auth is 0:
                try:
                    gauth = GoogleAuth("settings.yaml")
                    gauth.LocalWebserverAuth()
                    drive = GoogleDrive(gauth)
                    drive_auth = 1
                    unuploadable_uploader()

                except httplib2.ServerNotFoundError:
                    drive_auth = 0

            try:
                # noinspection PyUnboundLocalVariable
                f = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": fid}]})
                f.SetContentFile(f"{pictures_path}\\{tstamp_name + k + '.png'}")
                f['title'] = tstamp_name + k + ".png"
                f.Upload()

                # A bug due to which if the variable used to upload the file to gdrive isn't assigned 'None' as value (after uploading) the file
                # persists in the memory i.e. it can't be deleted during (current) program execution, as file would still reside in the memory
                f = None

            # In V.6 added the file create/append/write in UTF-8 (previously ASCII) encoding in order to incorporate the "꞉" in file
            except:

                # This conditon checks whether the UNUPLOADABLE_SCREENSHOTS.txt file exists or not
                if not os.path.isfile(f"{pictures_path}\\UNUPLOADABLE_SCREENSHOTS.txt"):
                    file = open(f"{pictures_path}\\UNUPLOADABLE_SCREENSHOTS.txt", 'w+', encoding='utf-8')
                    file.write(
                        "THIS FILE CONTAINS THE NAME OF ALL THE TIMESTAMP SCREENSHOTS THAT DIDN'T GOT UPLOADED TO THE GOOGLE DRIVE\n")
                    file.write("YOU CAN MANUALLY UPLOAD THE BELOW MENTIONED FILES TO GOOGLE DRIVE \n\n")
                    file.write(
                        "################################################################################################\n\n\n\n")
                    file.close()

                # This snippet of code adds the entry of the unuploaded screenshot in the UNUPLOADABLE_SCREENSHOTS.txt file
                log = open(f"{pictures_path}\\UNUPLOADABLE_SCREENSHOTS.txt", 'a', encoding='utf-8')
                log.write(tstamp_name + k + ".png\n")
                log.close()
