# README #

This is a read me about what each TIMESTAMP'er does and which is the best use case for each case.
Regardless of which version you are using, setting it up properly requires a little bit of Windows OS knowledge.
Each Timestamp'd program is of .pyw extension, which enables them to execute in the background without interference.
Code Could easily be optimized as it isn't coded most efficiently. I just wanted to make it memory-efficient,
therefore almost negligable amount of memory is used during their execution. 
The screenshot directory should not contain unnecessary files/folders as it may slow down the Timestamp process,
so it is advised to only store screenshots in it.


#   TIMESTAMP Screenshots V.1   #

* It involves taking a screenshot of the current screen discretely and naming it to the current date (DD-MM-YYYY).
* Makes it easier to Organise/Recognize screenshots as each one contains the date on which they are taken.
* Screenshots are taken by a shortcut defined by the user and not by the generic screenshot key (WIN + PrtScn)


How it works :

1) In the beginning, you have to assign a shortcut key in order to execute the Python script.

2) That is, you have to save your Python script in a location that can contain globally accessible shortcuts.
   Ex. C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\ is a directory that contains global shortcuts.

3) Then you have to manually assign a shortcut for your file by defining a shortcut for its execution in the shortcut 
   field that is found in its properties.

CONS: 1) It only works if the current application allows Windows global shortcuts; it won't work for applications that take keyboard focus control
          , ex. It won't work while watching a YouTube video in full screen / Playing a Video game in full screen.
       2) There is a delay (~2-5 sec) between the shortcut keypress and the screenshot capture as the Python file needs to be executed
       3) Timestamps will be added to the screenshots only if the Python script is called, i.e., if the user takes a screenshot using the generic 
          screenshot key (WIN + PrtScn), then the screenshot will be saved, but not with the Timestamps

I won't recommend this version to anybody as this version has a lot more drawbacks than the benefits. This version just acted as a 
pedalstone for the other version to come in the future.



#   TIMESTAMP Screenshots V.2   #


* This version was made on the first one but worked in a totally different way as compared to the previous one.
* This version works on the screenshot folder, i.e., a screenshot taken using the std screenshot key (WIN + PrtScn) will also be TIMESTAMP'd.
* This version removed the problem of focus control/loss as the std screenshot key is application-independent (works on all applications)


How it works :

1) You just have to place the Python script in the startup folder of your Windows OS(C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp). 
   So whenever your OS starts, this script starts executing.

2) It does file lookups on the screenshot folder to figure out whether a new screenshot is taken or not, and if it is taken, then it renames
   it to the current date.

CONS: Overtime the Screenshot folder will become unorganized with screenshots of different dates

This version suits almost everyone; if they can look aside, it's only a drawback. As it fulfills the main Aim of the whole project. Future versions
worked on this version and added new features to it. 



#   TIMESTAMP Screenshots V.3   #


* This version was made on the previous one (V.2), so it inherits all the features of the previous one and adds folder organization to it.
* This version starts in the same way as the previous one, but upon execution, does a lookup on the screenshot directory in order to figure out 
  whether there is a screenshot of the previous date (previous date < current date), and if it finds one, then it moves it to its month/date folder,
  and therefore keeps the main screenshot folder clean, as well as organizing the previous ones on their respective month and date folders.


How it works :

1) You just have to place the Python script in the startup folder of your Windows OS(C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp). 
   So whenever your OS starts, this script starts executing.

2) On execution, at first, it does a single lookup at the default screenshot directory of your Windows OS for searching any previous Timestamp 
   files

3) Upon finding one, it checks whether it was taken on a previous date than today. If it is true, then it moves the file to its months/date folder


This is the perfect version for anyone who wants to use one of these Scripts, as it fulfills all the requirements as well as works up 
on the drawbacks of its predecessor. I would definitely recommend it to everyone, and especially to those people who don't have a steady internet connection at all times while using their pc, as the next version makes use of it.   



#   TIMESTAMP Screenshots V.4   #


* This version was made on the previous one (V.3), so it inherits all the features of the previous one and adds Cloud storage to it.
* In this version, every screenshot taken during the execution of the program will be automatically uploaded to the specified folder in your Google
  Drive account. 
* Requires stable internet access at all times to be functional
* It ensures data retrieval when the local copy of the data (the one that is stored on your pc) is lost.
* Requires credential files like client_secret.json, settings.yaml, credential.json to be in the same directory as the Python script


How it works :

1) A batch file should be created in the startup folder, which contains some commands that execute the Python script that is stored at some other 
   safe directory
   
2) Upon execution, it verifies whether the given credentials of the Google Drive account are ok or not and gets the drive functionality ready according
   to it

3) When a screenshot is taken, it is timestamped, and a copy of it is uploaded to a Google Drive folder. The folder is determined by its folder ID


This version is for people who want data redundancy. Due to the small size of the screenshots you won't reach the storage cap of Google Drive
anytime before 5 - 10 yrs. I made this version personally for myself, and getting it working for others requires a lot of tweaking. Like getting
Googledrive credentials, client_secret, getting appropriate folder ID etc., which could be a lot of time-consuming as well as painful for a lot of people.
So, for those who don't care about data redundancy, cloud storage, blah blah blah. The TIMESTAMP Screenshot V.3 is the best for them.

CONS: If the TIMESTAMP screenshot is not uploaded due to poor internet connectivity/no internet access/server down, etc., the program crashes 


#   TIMESTAMP Screenshots V.5   # 


* This version works upon the drawbacks of the previous one (V.4) and, therefore, enables program execution till shutdown
* The working of this version is the same as V.4, but it adds a failsafe to it
* If the TIMESTAMP screenshot is not uploaded, then it makes an entry of the screenshot in a text file (UNUPLOADABLE_SCREENSHOTS.txt) and continues
  the program execution
* This UNUPLOADABLE_SCREENSHOTS.txt file is used for reuploading the screenshots that were not uploaded
* At internet availability, all the screenshot names in the UNUPLOADABLE_SCREENSHOTS.txt file get uploaded to the Google Drive 


How it works :

1) When a screenshot is unable to be uploaded on Google Drive, its entry is created in a separate text file

2) This text file contains the names of all the Timestamps that were not able to be uploaded to the Google Drive

3) At net availability, the names of the uploaded timestamp files are retrieved from this text file and are then uploaded to the Google Drive


This version enables the program to execute even if the screenshot is not uploaded but to rectify this, it notes the names of the screenshots that were 
not uploaded and then automatically uploads them when there is net availability. This version is recommended over the previous one, as it overcomes 
the drawbacks of the previous version. 


#   TIMESTAMP Screenshots V.6   #


* This version improvises a lot of aspects of the previous one (V.5) and allows for a lot more efficient program
* The structure of the program is still more/less the same, but every aspect of the code is optimized (made more efficient)
* V.5 only provided a failsafe if the program got executed successfully (during net access) and during the execution, the net connectivity issue arose.
  Now, even if the net connectivity hasn't been available since the beginning, the program will continue to execute (though cloud storage won't work)
* Removed the usage of datetime and PIL.Image module (2 of the most important ones), where datetime was just redundant due to the time module's availability
  and PIL.The Image wasn't much needed (most of its working got replaced by functions inside the os module)
* This version made use of Environment variables for resolving paths, due to which this version is not User sensitive (i.e., all absolute paths
  are replaced by paths created dynamically for an OS, using Env. variables like %userprofile%)
* Fixed the bug, due to which the most recent file that was uploaded to GDrive can't be deleted (as it was still in the memory)
* Previous versions of Timestamp Screenshot used a 5-second bottleneck on the while loop and then searched for new Screenshots. This is changed
  in the current version. Now, it uses the creation date of the file in order to get the Timestamp values (this allows for accurate timestamps)
* Followed PEP guidelines and reduced the number of except clauses in the code, instead made the exceptions specific (ex:- httplib2.ServerNotFoundError)
* Changed the way timestamps are represented by following ISO 8601 Timestamp format standard
* This version also adds time to the Timestamp, i.e., now files would not only have the current Date but also the current time. Therefore, now the,
  timestamp format is YYYY-MM-DD hh:mm:ss (x) ((x) is optional)
* Now, files are created/stored/modified with UTF-8 encoding. The reason for it being that, as mentioned in our previous point, our Timestamp now contain
  the time of creation as well (which previously was only the Date), and time is stored as hh:mm:ss, and since Windows doesn't allow a : (colon) in the 
  filename, I had to get an alternative for that character, so I found : (......), which looks exactly like a colon and is supported in the Windows file name
* Replaced normal or formatted strings with f" strings, which are faster than the previous ones and improve readability

How it works:  Working is the same as the previous one.



This version didn't introduce new features to the Timestamp project but worked on limitations of V.5. I finally decided to create a formal version out 
of it as further changes would make the comment/documentation cryptic and hard to create, and the amount of changes are so many that some of them slip 
through the documentation process. All the improvements were made over time with usage. 

Explanations of changes and why they were made :


1) The current version uses a checksum on whether the OAuth credentials have been authenticated or not and uses a try-except clause for that purpose. This
   allows the program to continue execution even if the credentials have not been authenticated. The process of Authentication being successful or not is
   determined by the value of a variable whose value is 0 if the Authentication is not successful and 1 if it is successful; this value is used later in the
   program to enable reauthentication if it has not been already done.

2) Removed the datetime module from the program; the time module's functions replaced all of its usage. Due to the bottleneck of 5 sec (Time. sleep(5))
   time module has to be imported, and since the time module incorporates almost all of the functioning of the datetime module, I ditched datetime.

3) Removed the PIL module from the program, as I realized that nothing in place of "Image Processing" is being done in the program. All the usage of PIL (Image)
   has been replaced by the os module's functions. It may be kind of hard to understand how an Image processing module got replaced by an os module, but in 
   practice, no image processing was done inside the program. The program opened the image files (Screenshot files) via the Image.open() provided by PIL,
   and then save them by changing the name Image. Save ("different_name"), and then delete the original file. So "just for changing filenames" PIL.Image 
   isn't the most generic tool. Therefore, I replaced all the occurence of PIL. Image by os. rename(), which was way faster and didn't have to load the Image 
   to do the process. This method is far more robust than the previous one; as for this, the file need not have to be opened for the process. All the os does is 
   change the metadata of the file containing its filename. This method even preserves the metadata (Time, atime, mtime etc.) of the original file, as
   previously, a new file was created by Image.save(), which had a completely different ctime, atime etc., than the original one. 

4) Environment variables were used at the beginning of the code. This allowed for getting the Default user directory of different users a lot easier as 
   now the program just calls the %userprofile% environment variable to get the path, rather than using hardcoded paths that were User sensitive. This
   method (to my knowledge) works for any Windows 10 & 8 as both of them use the same default path for storing the screenshots. Previous versions of windows
   , by default, didn't allow taking shortcuts using hotkeys. 

5) A bug exists in the pydrive module, due to which we can't delete the file that was most recently uploaded to googledrive if the variable used for the upload
   isn't assigned the value  None. Due to this, one can't delete the file that was just uploaded on Gdrive from his PC, as the file is still open in the memory.
   To fix this, the variable that was used in the creation and upload of the file on GDrive has been assigned the value of None, after which the file attains its 
   normal state, and hence allows its deletion.

6) A lot of except: were replaced by except {exception}. As the PEP guidelines state, the usage of except: should be avoided as it not only catches
   exceptions but even errors such as one arose due to syntax, OSError etc. Therefore, it is advised to mention the exception explicitly in most cases
   as it streamlines the code and prevents unwanted errors from being inhibited from the User.

7) Previously, timestamps were created out of current
   Date only, and the Date was not of creation of the Screenshot, but was the Date in which the program got access to that Screenshot. This method posed 
   several problems; firstly, if a lot of screenshots are being taken, all of them are just saved as Date (x), which is good, but it just specifies the Date 
   when those screenshots were taken and not the exact Time of the Date. Secondly, V.5 was only applicable assuming that the program was already running when
   the screenshots were taken (so that it could stamp the current Date on them); if for some reason the program wasn't running when the screenshots were taken,
   then the screenshots stay as it is and they were timestamped on the next time the program is executed. This causes a problem as now the Timestamp will have 
   incorrect date info (as it was timestamped on some other date, not the actual one). If the dates change during the program execution, then there is
   a small chance that an incorrect Timestamp will be applied to Screenshots that were taken just as the dates change. Ex. if one Screenshot was taken at 
   10-10-2010 at 23:59:58, and then the program waits (not necessary) for the next 5 seconds and timestamps, then the Screenshot would have incorrect 
   Timestamp as now the Date would be ~11-10-2010 [00:00:0x] (the Date has been changed). In V.6, the program uses the date/time of creation of the file
   in order to get its Timestamp of creation. Due to this, the files are no longer dependent on the program to timestamp them at the right time. Rather the 
   metadata stored by them would act as a timestamp for them at any time in the future. This method is far superior as we no longer depend on the current Date.
   The files could be Timestamp'd at any time in the future and would still possess the correct Timestamp (unless they have been tampered with). 

   ** Due to (3) and (7), now the ctime and filename can be crosschecked to ensure the authenticity of the Timestamp.

8) Changed the way how timestamps were made. Now, ISO 8601 Timestamp syntax will be followed in the current/later iterations of the Timestamp project. This
   allowed the Timestamp files to be easily understandable by any other user and prevented ambiguity, which may arise out of its syntax. 

9) In ISO 8601 Timestamp Syntax, the Timestamp would be of the format YYYY-MM-DD hh:mm:ss. Our previous Timestamps were of syntax DD-MM-YYYY 
   and didn't have time in their format. The addition of Time in Timestamps allows for the timestamps to be a lot more specific on what point of the day they were taken.
   The details of its Timestamp are obtained by getting the creation data (date/time) of the original screenshot file.

11) The UNUPLOADABLE_SCREENSHOTS.txt file, which was used to reupload the screenshots that weren't uploaded previously, was encoding ASCII. Now it has 
    been changed to UTF-8. The reason for it being that in order to follow the ISO 8601 syntax, our timestamps would be of syntax YYYY-MM-DD hh:mm:ss. The time 
    quantities are separated from each other via a : (colon). Windows does not allow a : in its file/folder name; therefore, I had to choose an equal-looking 
    alternative for a colon, which was ꞉ (U+A789) (Modified Letter Colon), which is a character that looks similar to a colon and is eligible for usage in a filename
    but is only accessible on larger scoped encoding schemes(UTF-8/16/32). So a hypothetical timestamp 2000-10-20 10:10:12, which was not uploaded, would have 
    an entry in UNUPLOADABLE_SCREENSHOTS.txt, but since the file was of ASCII encoding, it couldn't represent ꞉ (U+A789) properly (ASCII could only 
    represent 256 unique characters, and ꞉ isn't one of them). So, in order to incorporate the ꞉ in our file, we had to format the file with an 
    encoding like UTF-8, which supports larger character sets.


Some improvements which may be upcoming:-

[1] Currently, a list of files is created, and then it is matched with the fnmatch() pattern, which is a waste as we are only interested in files matching the 
    timestamp syntax. So, I would like to replace it with something like an iterator in the future.

[2] fnmatch() is lenient when it comes to matching syntax. As of now it would match anything which got matched by the pattern *-*-*.png. This allows 
    for false positives like 12312-123123124-24124 or asdfa-]dpd]ad;-dflkls123 (as the * in the pattern means any character). I would like to make this 
    pattern a lot more strict by using a regex-like pattern matching for checking authentic timestamps, but which could be used with [1] and would be more 
    efficient. (fnmatch() also allows for a strict timestamp syntax, but it is a lot more lengthy and messy than a regex equivalent, as fnmatch does not have
    repeating qualifiers. Therefore, every character/class has to be written explicitly)

