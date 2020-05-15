print("Type Calculator to Open the Calculator or type Reboot to Reboot the script.")
Command = input("> ")
if Command == "Calculator":
   exec(open("calculator.py").read())
elif Command == "Reboot":
   exec(open("main.py").read())
