from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
import re

# PATH = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH)

def chrome():
    driver_option = Options()
    driver_option.add_argument('--no-sandbox')
    driver_option.add_argument('--disable-dev-shm-usage')
    driver_option.add_argument('--disable-gpu')
    driver =  webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver.exe',options=driver_option )
    return driver

def datapick(url,driver):
  driver.get(url)
  time.sleep(1)
  soup = BeautifulSoup(driver.page_source, 'html.parser')
  main = soup.find('div', {'class':re.compile(r'results-view')})
  data = main.findAll('div', {'class':re.compile(r'lf-item-container listing-preview type-cars-for-sale')})
  print(len(data))

  for elt in data:
      nom_article = elt.find("h4", {"class": "case27-secondary-text listing-preview-title"}).get_text()
      print(nom_article)
      lien_image = elt.a['href']
      print(lien_image)
      time.sleep(2)
      try:
        price = elt.find('div', {'class': 'rent-price inside-rent-price'}).get_text()
        print(price)
        endurance = elt.find('ul', {'class':'details-list'}).get_text()
        print(endurance)
      except:
        price = 0
        endurance = "null"
      localisation = elt.find('span', {'class':'category-name'}).get_text()
      print(localisation)
      print("---")

# for i in range(1,134):
#   datapick("https://gasycar.com/voiture-occasion/?sort=latest")
#   datapick("https://gasycar.com/voiture-occasion/?pg={}&sort=latest"+str(i))
driver = chrome() 
datapick("https://gasycar.com/voiture-occasion/?pg=1&sort=latest",driver)
datapick("https://gasycar.com/voiture-occasion/?pg=2&sort=latest",driver)
datapick("https://gasycar.com/voiture-occasion/?pg=3&sort=latest",driver)



    

      


