# mensaVegIlmenau
This is a simple webcrawler to extract the vegan menu from the Mensa Eherenberg (TU Ilmenau) webseite and post ist content to a Telegram Group
13.12.2021

# Install:
Install Selenium https://realpython.com/modern-web-automation-with-python-and-selenium/		pip install selenium


download and install geckodriver for your system
https://github.com/mozilla/geckodriver/releases/
move it to the right path

Mac:
/usr/local/bin

Windows:
- install WebDriver (Option 1: use geckodriver.exe in "Driver" folder, use Python code).
					(Option 2: Download geckodriver (https://github.com/mozilla/geckodriver/releases), Add PATH to python using BASH command (not used)).

To start the mainBosch.py Script, you just insert your Bot API token. After you installed the requirements.txt

like e.g.

python3 mainBosch.py 1234567:djkfbkjr4hoohfffjoe <---- herer your API Telegram Bot_Token

And than you get the food info you wanted at 11:30 AM to the group or Bot-chat you wrote right before starting the script. (but your Bot needs to be in that group ;)) 
