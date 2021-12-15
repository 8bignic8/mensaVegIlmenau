# from selenium import webdriver

# driver.get('https://www.stw-thueringen.de/mensen/ilmenau/mensa-ehrenberg.html')

# find_searchbox = driver.findElement(By.id(“text-box”));

import time
import argparse
import os

def remind(h,m):
    te = time.localtime() #asks the local computer time
    if((te.tm_hour == h) and te.tm_min == m):
        return True

json_config_path = "config.json"
parser = argparse.ArgumentParser(description='Input of the Telegram_Bot token')
parser.add_argument('Telegram_Bot_Token', metavar='-t', nargs='?', const=1, type=str, help='A string seperated by : ')
## TO DO add args for houer and min
args = parser.parse_args()
if(args):
    Telegram_token = args.Telegram_Bot_Token

if(not(os.path.isfile(json_config_path))):
    os.system("python3 main.py " + Telegram_token)
while(True):
    if(remind(11,30)):
        os.system("python3 main.py")
        time.sleep(65)
    time.sleep(55)