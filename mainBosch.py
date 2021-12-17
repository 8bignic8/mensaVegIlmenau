# from selenium import webdriver

# driver.get('https://www.stw-thueringen.de/mensen/ilmenau/mensa-ehrenberg.html')

# find_searchbox = driver.findElement(By.id(“text-box”));

import time
import argparse
import os
from main import updateConfig as upconf
from main import writeConf
from main import loadConf
from main import jsonConfIsNotavalable as isconfNot

def remind(h,m):
    te = time.localtime() #asks the local computer time
    if((te.tm_hour == h) and te.tm_min == m):
        return True

json_config_path = "config.json"

parser = argparse.ArgumentParser(description='Input of the Telegram_Bot token')

parser.add_argument('Telegram_Bot_Token', metavar='-t', nargs='?', const=1, type=str, help='A BOT TOKEN string seperated by : ')
parser.add_argument('hour_inp', metavar='-ho', nargs='?', const=1, type=int, help='Type in the hour when you want to send the current food')
parser.add_argument('min_inp', metavar='-mi', nargs='?', const=1, type=int, help='Type in the minute when you want to send the current food')

args = parser.parse_args()

if(args):
    Telegram_token = args.Telegram_Bot_Token
    hour = args.hour_inp
    minutes = args.min_inp

    if(isconfNot(json_config_path)): ## if there is no conf avalable make new one and add parameters
        #search for the Chat ID
        os.system("python main.py " + Telegram_token)
        # Load and write in the generated config.json the hour and minute
        config = loadConf(json_config_path)
        config = upconf(config, 'hour', hour)
        config = upconf(config, 'minutes', minutes)

        # save to file, with path json_config_path
        writeConf(config,json_config_path)

    else: ## There is a config, load and update according to args
        config = loadConf(json_config_path)
        config['hour'] = hour
        config['minutes'] = minutes
        config['token'] = Telegram_token
        #save
        writeConf(config)

# no args given
else:
    try:
        config = loadConf(json_config_path)
        # Loads from config.json the hour and minute
        hour = config['hour']
        minutes = config['minutes']

    except:
        print('Error there is no config.json, please insert the Arguments after the mainBosch.py or add a config.json')

while(True):
    if(remind(hour,minutes)):
        os.system("python3 main.py")
        time.sleep(65)
    time.sleep(55)