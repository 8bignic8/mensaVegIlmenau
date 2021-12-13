# from selenium import webdriver

# driver.get('https://www.stw-thueringen.de/mensen/ilmenau/mensa-ehrenberg.html')

# find_searchbox = driver.findElement(By.id(“text-box”));

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
fro

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(executable_path=r'gdriver/geckodriver', options=options)
driver.get('https://www.stw-thueringen.de/mensen/ilmenau/mensa-ehrenberg.html')

element=driver.find_element(By.ID,"speiseplan")