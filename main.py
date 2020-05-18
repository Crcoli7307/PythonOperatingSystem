import sentry_sdk
sentry_sdk.init("https://e935fd3f98b54c52be5f96f6b5bc890b@o394689.ingest.sentry.io/5245135")
print("Welcome to Python Operating System!")
print("Importing Services...")
import time
import datetime
print("Loading...")
Date = datetime.date
Time = datetime.time
sleepTime = time.sleep
currentDT = datetime.datetime.now()
currentVersion = "0.0.2"
currentVersionType = "Alpha"
print("Imported Variables...")
print("The current time is:")
print(str(currentDT))
timeCorrect = input("Correct? (y/n)\n")
if timeCorrect == "y":
  print("Time and Date: [PASS]")
  print("Waiting for Internet Connection...")
  if currentVersion == "0.0.1" or currentVersion == "0.0.2":
    print("No Internet Connection Needed...") #Alpha  Version Does not Have Internet Connection
    print("Internet Connection: [FAIL]")
    print("Continuing With Boot...") 
    print("Current Revision:", currentVersion)
    if currentVersionType == "Alpha":
      print("This operating system is in Alpha.")
      print("Username and Password Save Not Available")
      print("Starting Login Service...")
      exec(open("login.py").read())
    elif currentVersionType == "Beta":
      print("This operating system is in Beta.")
      print("Username and Password Save Not Available")
      print("Starting Login Service...")
      exec(open("login.py").read())
    else:
      print("A critical error has ocurred! Code: ERRINVOSVERTYPE")
  else:
    print("A critical error has ocurred! Code: ERRINVOSVER")
else:
  exec(open("main.py").read())
