#### TO DO

## Price adding
## Printing to Telegram
### Essens container einzeln bearbeiten
### Save the food over the year

####
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import json
import telegram_send
import requests
import argparse
import os

json_config_path = "config.json"

def updateConfig(conf, name, value):
    conf = conf.copy()  # copys the current dict to itself and than
    conf.update({name: value})  # adds the current dict
    writeConf(conf)
    return conf

def writeConf(conf):
    try:
        with open('config.json', 'w', encoding='utf-8') as f: #writing config.json in utf-8
            json.dump(conf, f)
    except:
        print('config file write error')
def loadConf(json_config_path):
    #### reads config.json
    with open(json_config_path, 'r') as j:
        con = json.loads(j.read())
    return con

def sendTGMessage(Message, config):
    # https://stackoverflow.com/questions/41174831/telegram-bot-chat-not-found
    method = 'sendMessage'
    Message = str(Message)
    response = requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(config['token'], method),
        data={'chat_id': config['myuserid'], 'text': str(Message)}
    ).json()

if(not(os.path.isfile(json_config_path))): ##checks if file is available
    noConfig = True
    print('Adding the arguments to == > config.json')
else:
    noConfig = False
    print('Loading existing conf')
    config = loadConf(json_config_path)

##adding the arguments
if(noConfig):
    parser = argparse.ArgumentParser(description='Input of the Telegram_Bot token')
    #https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
    #parser.add_argument('Telegram_Bot_Token', metavar='-t',nargs='?', const=1,  type=str, default= '5083693463:AAGW-VqK4_l_uH8pC_H3GrLqTQOi0v61xjc',
     #                   help='A string seperated by : ')

    parser.add_argument('Telegram_Bot_Token', metavar='-t', nargs='?', const=1, type=str,
                        help='A string seperated by : ')

    args = parser.parse_args()
    if(args):
        Telegram_token = args.Telegram_Bot_Token
        a = os.system("python3 ./find_telegram_chatID/setConfig.py "+Telegram_token) ## generates the config.json with the telegram function
    config = loadConf(json_config_path)

config = updateConfig(config, 'website', 'https://www.stw-thueringen.de/mensen/ilmenau/mensa-ehrenberg.html')
config = updateConfig(config, 'property_a', 'Vegane') ## what the script searches for
config = updateConfig(config, 'property_b', 'Vegetarisch') ## what the script searches for
config = updateConfig(config, 'property_c', '-1') ## what the script searches for


options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(executable_path=r'gdriver/geckodriver', options=options)  ## path to the gdriver
driver.get(config['website'])#'https://www.stw-thueringen.de/mensen/ilmenau/mensa-ehrenberg.html')

foodPlan_html=driver.find_element(By.ID, "speiseplan") ## https://pythonbasics.org/selenium-find-element/

allMeals = foodPlan_html.find_elements(By.CLASS_NAME, "container")

#foodN = allMeals[0]#.find_element(By.CLASS_NAME, "mealText")
j = 0
foodList = {}
while(len(allMeals) >= j):
    try:
        if(allMeals[j].find_element(By.CLASS_NAME, "splIconMeal") is not None):
            a = allMeals[j].find_elements(By.CLASS_NAME, "splIconMeal") ##
            propApply = False
            for item in a:
                #print(item.get_attribute("alt"))
                ###TO DO check if some Zusatzstoffe or Allergene
                if((config['property_a'] in item.get_attribute("alt")) or
                        (config['property_b'] in item.get_attribute("alt")) or
                        (config['property_c'] in item.get_attribute("alt"))):
                    #property = property + ' and ' + item.get_attribute("alt")
                    propApply = True

            if(propApply):
                # https://www.w3schools.com/python/python_dictionaries.asp
                foodList = foodList.copy()  # copys the current dict to itself and than
                foodList.update({(len(foodList) + 1): allMeals[j]})  # adds the current dict
                propApply = False
    except:
        pass
    j = j + 1

foodNames = foodPlan_html.find_element(By.CLASS_NAME, "mealText")
additives = foodPlan_html.find_elements(By.CLASS_NAME, "zusatzstoffe")
price = foodPlan_html.find_elements(By.CLASS_NAME, "mealPreise")

foodProperties_all = foodPlan_html.find_elements(By.CLASS_NAME, "splIconMeal") ##


#print(foodList[1].text)
h = 1
sendTGMessage('Das '+ config['property_a'] +' Essen des Tages ist:', config)
while(len(foodList)>=h):

    sendTGMessage(foodList[h].text, config)
    if(h==2):
        sendTGMessage('Oh sogar noch eins mehr \U0001F601', config)
    h = h + 1

driver.close() ## cloese the webbrowser instance
exit()