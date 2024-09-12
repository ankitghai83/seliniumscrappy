import pandas as pd
from selenium import webdriver # allow launching of browser
from selenium.webdriver.common.by import By # allow search with parameter
from selenium.webdriver.support.ui import WebDriverWait #allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation
from selenium.webdriver.chrome.service import Service # This is used to pass executable path

#Prepare the code for easily opening new browser window (This will be useful when we are doing parallelization)

driver_option = webdriver.ChromeOptions()
driver_option.add_argument("--incognito") # This is open url without any pop up
chromedriver_path="C:\\Users\\Ankit Ghai\\Documents\\PycharmProjects\\pythonProject\\allpythonproject\\seliniumwebdriver\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
service  = Service(executable_path=chromedriver_path)


def create_webdriver():
    driver=webdriver.Chrome(service=service, options=driver_option)
    driver.get("https://github.com/collections/machine-learning")
    #WebDriverWait.until(5)
    projects=driver.find_elements("//h1[@class='h3 lh-condensed']")

    project_list={}
    for proj in projects:
        proj_name=proj.text
        proj_url=driver.find_elements("a")[0].get_attribute('href')
        project_list[proj_name]=proj_url
    return project_list

 


create_webdriver()

