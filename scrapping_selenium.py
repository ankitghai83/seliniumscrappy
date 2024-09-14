import pandas as pd
from selenium import webdriver # allow launching of browser
from selenium.webdriver.common.by import By # allow search with parameter
from selenium.webdriver.support.ui import WebDriverWait #allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation
from selenium.webdriver.chrome.service import Service # This is used to pass executable path
import time

#Prepare the code for easily opening new browser window (This will be useful when we are doing parallelization)

driver_option = webdriver.ChromeOptions()
driver_option.add_argument("--incognito") # This is open url without any pop up
chromedriver_path="C:\\Users\\Ankit Ghai\\Documents\\PycharmProjects\\pythonProject\\allpythonproject\\seliniumwebdriver\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
service  = Service(executable_path=chromedriver_path)


try:
    def create_webdriver():
        driver=webdriver.Chrome(service=service, options=driver_option)
        driver.get("https://github.com/collections/machine-learning")

        #WebDriverWait.until(5)
        projects=driver.find_elements("xpath","//h1[@class='h3 lh-condensed']/a")
        #links=driver.find_elements(By.XPATH, "/html/body/div[1]/div[5]/main/div[2]/div/div/article[1]/div[1]/h1")
        #print(projects)
        #return projects
        time.sleep(3)
    
        project_list={}
        for proj in projects:
            proj_name=proj.text
            #proj_url=proj.find_elements("xpath","/html/body/div[1]/div[5]/main/div[2]/div/div/article[4]/div[1]/h1/a").append
            proj_url=proj.get_attribute('href')
            print(f"Project: {proj_name}, URL: {proj_url}")
            #links=[elem.get_attribute('href') for elem in proj_url]
            project_list[proj_name]=proj_url
            project_df=pd.DataFrame.from_dict(project_list,orient='index')
            project_df['proj_name']=project_df.index
            project_df.columns=['proj_url','proj_name']
            project_df=project_df.reset_index(drop=True)
            #print(project_df)
            project_df.to_csv('project_list.csv')
            #browser.quit()
    
except Exception as es:
    print("The error is: ",es)

 


create_webdriver()

