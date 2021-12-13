from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'Driver\geckodriver.exe')
driver.get('https://www.stw-thueringen.de/mensen/ilmenau/mensa-ehrenberg.html')
