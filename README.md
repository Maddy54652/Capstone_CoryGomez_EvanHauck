# Capstone_CoryGomez_EvanHauck
**Synopsis:**

This code is a Capstone Senior Project designed to transfer data from a weather station on campus at CSUCI to an outside database that is accessed by a front end designed by this code. This project uses Django Python which is a combination of Python 3.5.5, HTML, CSS, and some Java Script to manage the full stack operations of this project. The directory labeled Raspberry Pi is not ment to be ran on the same system as the rest of the project but to be ran from a seperate Raspberry Pi module that we have set up on campus to send out the data that is necessary.

**Finished Product:**

[Link to Web Page](http://esrm.herokuapp.com/)

**Installation:**

Django needs to be installed on the computer used to edit/run this project. We used the PyCharm ide since it has a very easy to use interface and has a free 1-year subscription for Students (If you use PyCharm it is reccomended not to use Windows 8 or above since the file management system does not work well with the PyCharm framework and constantly throws errors when testing the project even if the project has no errors. It would be IDEAL to use linux preferrebly Ubuntu or Mint). Also Python 3 must be installed on the computer as well or else the code would not be able to compile since it would not have an interpreter to read the code. Mysql driver and server install is also a must since the project uses a mysql style database. Lastly you must install pip before beginning any coding with Django. Pip allows you to install python dependencies that are not included in the original Python 3 libraries. The requirements.txt file holds the dependencies that are crucial for running this specific program which you must install through pip (The requirements.txt file is also used for Heroku to deploy the website created by this project by telling the Heroku servers which dependecies are needed to run the code). If for some reason during debugging you reach an error that goes along the lines of "settings.config not defined" that is a PyCharm specific error that comes up when the container (*The file the Python code is in*) you are testing has not yet configured the settings to the project settings directory. Since the main projects directory for this specific project is *Capstone*, to get around this error you open up *edit configuration* and add to *Environment Variables* **DJANGO_SETTINGS_MODULE=Capstone.settings**

**Tips and Notes:**

Since we are running the data retrival code off of a Rasberry Pi, we ran into the issue of the code needing to run on startup without user input and to restart when encountering a disconnection of power or internet source. We found a solution deep in the internet which we decided to put here for convenience purposes.
1. First start out making a text file on the desktop for the Raspberry Pi that is labled *unique-name*.sh and in that file on the first line write *cd* and the second line *sudo nano .bashrc* **(this is so you can make an executable file to undo step 4 in the case that you need to use the terminal because after you complete step 4 you will not be able to run anymore commands through terminal)**
2. Open up terminal and type *cd Desktop* and then enter in *sudo chmod 755 *unique-name*.sh (this will make the newly made file an executable file that you can click with a mouse to execute in terminal to bypass rebooting the device)
3. Now we open the autostart file to edit the file to force terminal to open when the device boots *sudo nano /etc/xdg/lxsession/LXDE-pi/autostart* and at the bottom add the line *@lxterminal*
4. Go back to root directory *cd* then *sudo nano .bashrc* (or you can simply click on the newly made executeable file) and in the bottom of the file enter in *python /path/to/python/file/file.py* and on the next line *sudo reboot* this will make it so that everytime the new terminal is opened, it will run your code and if for any reason the code breaks it will automatically reboot the device

**Resources:**

[Tutorial/API For Django](https://www.djangoproject.com/start/)

[Pycharm Download Site](https://www.jetbrains.com/pycharm/download/)


**Contributors**

Cory Gomez (cory.gomez257@gmail.com) Linkedin - [Cory's Linkedin Account](https://www.linkedin.com/in/cory-gomez-146054117)

Evan Hauck (Evan.hauck5@gmail.com) Linkedin - [Evan's Linkdedin Account](https://www.linkedin.com/in/evan-hauck-30a9b0a9)
