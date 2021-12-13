#### TO DO

## Price adding
## Printing to Telegram
### Essens container einzeln bearbeiten
#### 

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(executable_path=r'gdriver/geckodriver', options=options)
driver.get('https://www.stw-thueringen.de/mensen/ilmenau/mensa-ehrenberg.html')

foodPlan_html=driver.find_element(By.ID, "speiseplan") ## https://pythonbasics.org/selenium-find-element/
foodNames = foodPlan_html.find_elements(By.CLASS_NAME, "mealText")
additives = foodPlan_html.find_elements(By.CLASS_NAME, "zusatzstoffe")
price = foodPlan_html.find_elements(By.CLASS_NAME, "mealPreise")

foodProperties_all = foodPlan_html.find_elements(By.CLASS_NAME, "splIconMeal") ##

#foodProperties_all[0].get_attribute("alt")

def checkProp(property, foodList):  #checks if the list has the wanted property
    check = False
    for item in foodList:
        loop_property = item.get_attribute("alt")
        if (property == loop_property):
            check = True
    return check

#print(foodProperties)

#infoB = info.find_elements(By.CLASS_NAME, "")
print(dir(foodProperties))

def isVegan():
    pass ## TO DO

def printText(itmens):
    for item in itmens:
        print(item.text)
printText(foodNames)
printText(additives)
printText(foodProperties)

driver.close() ## cloese the webbrowser instance