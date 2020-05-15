print("Welcome to Python Operating System!")
print("Importing Services...")
import time
import datetime
print("Loading...")
Date = datetime.date
Time = datetime.time
sleepTime = time.sleep
currentVersion = "0.0.1"
currentVersionType = "Alpha"
print("Imported Variables...")
currentDT = datetime.datetime.now()
print("The current time is:")
print (str(currentDT))
timeCorrect = input("Correct? y/n\n")
if timeCorrect == "y":
  print("Time and Date: [OK]")
  print("Waiting for Internet Connection...")
  if currentVersion == "0.0.1":
    print("No Internet Connection Needed...") #Alpha  Version Does not Have Internet Connection
    print("Internet Connection: [FAIL]")
    print("Continuing With Boot...") 
    print("Current Revision:", currentVersion)
    if currentVersionType == "Alpha":
      print("This operating system is in Alpha.")
      print("Username and Password Save Not Available")
      print("Starting Login Service...")
      exec(open("login.py").read())
      
