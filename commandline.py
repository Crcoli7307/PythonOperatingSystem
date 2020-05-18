import datetime
currentDT = datetime.datetime.now()
print("Welcome to the command line! Make sure to type the name of the application exactly! For a list of apps, type: listapps")
apps = "Notepad, Calculator, Time, Reboot"
Command = input("> ")
if Command == "Calculator" or Command == "calculator":
   exec(open("calculator.py").read())
elif Command == "Reboot" or Command == "reboot":
   exec(open("main.py").read())
elif Command == "Notepad" or Command == "notepad":
    exec(open("notepad.py").read())
elif Command == "listapps":
  print(apps)
  exec(open("commandline.py").read())
elif Command == "Time" or Command == "time":
  print(str(currentDT))
  exec(open("commandline.py").read())
else:
  print("A critical error has ocurred! Code: ERRINVCMD")
  time.sleep(1)
  print("Rebooting Command Line...")
  exec(open("commandline.py").read())
