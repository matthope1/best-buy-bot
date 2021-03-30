from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Read credit card info from data file

# f = open("data.txt", "r")
# print("reading data from file...")
# print(f.read())
# print("done reading data!")


option = webdriver.ChromeOptions()


#Removes navigator.webdriver flag

# For older ChromeDriver under version 79.0.3945.16
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)

#For ChromeDriver version 79.0.3945.16 or over
option.add_argument('--disable-blink-features=AutomationControlled')


driver.get("https://www.bestbuy.ca/en-ca/product/apple-macbook-air-13-1-6ghz-intel-core-i5-8gb-ram-256gb-storage-2019-model-refurbished-grade-a/15265626?icmp=Recos_3across_tp_sllng_prdcts&referrer=PLP_Reco")
print(driver.title)
isComplete = False

while not isComplete:

  try:
    atcBtn = WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.CSS_SELECTOR,'#test > button'))
    )
    isComplete = True;
    print("button is clickable")

    atcBtn.click()
  except:
    print("except")
    continue
