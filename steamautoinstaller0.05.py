#	PLEASE READ THIS FIRST, NOTHING WILL WORK IF YOU DONT!!!:

# 	IF YOU DONT WANT TO READ, WATCH MY QUICKSTART VIDEO HERE: https://youtu.be/gvNXnEhqf8U

#	WARNING: this probably only works on a 1920x1080 screen, you would probably have to do a fuckton of work to make it work on other 
#	screens, i dunno.

#	DEFINITELY READ THIS SECOND:

#	Please, select which disk you're gonna be downloading BEFORE you run the script and make sure ALL your games are uninstalledor shits gonna happen
#	(do a "test download", and then itll say "install under C:/user/steamBS", change that to D:/ if youll be using a hard drive. THEN CLICK DOWNLOAD, then cancel download/uninstall)



#	i believe thats it, if somethings not working email me at skepticseptic1@gmail.com WITH THE SUBJECT "steam auto installer" (if its a different subject i will probably ignore it)
#	and lastly, feel free to reverse engineer this however you want, enjoy!


#ACTUAL WORK________________________________________________________________________________________________________________________________________________________________________________________

#imports
import time
import pyautogui
#importsEND



#quick error message
print("IF NOTHING WORKS, OPEN steamautoinstall.py WITH NOTEPAD \n THERE YOU WILL FIND HOW TO MAKE THIS SHIT LIKE WORK N STUFF. AFTERWARDS OPEN WITH PYTHON 3.10 \n and please move this prompt down and to the left a bit. \n")
time.sleep(5)
fav = int(input("How many favorite games do you have? (at the very top, 'FAVORITES (#)')\n"))
unc = int(input("How many uncategorized games do you have? (somewhere in the middle, 'UNCATEGORIZED (#)')\n"))
print("Last warning, promise: \n please fullscreen steam and click back onto here")
time.sleep(5)
print("Thank you, downloads will now begin. This process will take 2-5 minutes.")
time.sleep(2)
print("\n \n WARNING: YOU WILL NOT BE ABLE TO USE THIS PC FOR 2-5 MINUTES ONCE THIS STARTS \n 'PRESS CTRL + C' TO END NOW")
time.sleep(4)
print("STARTING IN")
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
#errormessageEND

#variables
gx = 100
gy = 240
installx = 350
instally = 420
install2x = 1050
install2y = 680 
#variablesEND


#heres a pause you can make to prep you for intense file downloadingggg or smth idk

#pause
time.sleep(0)
#pauseEND

#SO here its gonna click the library on a standard 1920x1080 screen

#click library
pyautogui.click(200,50)
#click libraryEND

time.sleep(1)

#OK so this is where it clicks the first game

#click game1/CALIBRATION
pyautogui.click(gx,gy)
#click game1END

time.sleep(1)

#click big blue install button
pyautogui.click(installx, instally)
#clickinstallEND

time.sleep(1)

#click grey continue button
pyautogui.click(install2x, install2y)
time.sleep(1)
pyautogui.click(install2x, install2y)
#clickginstallEND

#REPEAT INSTALLING, no comments as its the same as above shit but over and over again:

time.sleep(7)

for i in range(fav):
	pyautogui.click(100, 120)
	pyautogui.typewrite(["down"])
	time.sleep(1)
	pyautogui.click(installx, instally)
	time.sleep(1)
	pyautogui.click(install2x, install2y)
	time.sleep(1)
	pyautogui.click(install2x, install2y)
	time.sleep(7)
	
	
pyautogui.typewrite(["down"])

for i in range(unc):
	pyautogui.click(100, 120)
	pyautogui.typewrite(["down"])
	time.sleep(1)
	pyautogui.click(installx, instally)
	time.sleep(1)
	pyautogui.click(install2x, install2y)
	time.sleep(1)
	pyautogui.click(install2x, install2y)
	time.sleep(7)
	