print("----LogIn Service----")
print("Checking for saved user info...")
#User Info Not Saveable in versions below V0.0.3
Username = input("Create a Username:\n")
if Username == "" or Username == " ":
  print("Username can't be empty!")
  exec(open("login.py").read())
Password = input("Create a Password:\n")
if Password == "" or Password == " ":
  print("Password can't be empty!")
  exec(open("login.py").read())
print("Saving User Info...")
print("User Info Not Saveable in versions below V0.0.3")
print("Starting Main Boot...")
print("Ⓦ ⓔ ⓛ ⓒ ⓞ ⓜ ⓔ   ⓣ ⓞ   Ⓟ ⓨ ⓣ ⓗ ⓞ ⓝ   Ⓞ Ⓢ !")
print("Welcome,", Username,"to Python OS!")
exec(open("commandline.py").read())
