import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = uc.Chrome()
driver.get('https://www.bestbuy.ca/en-ca/product/apple-macbook-air-13-1-6ghz-intel-core-i5-8gb-ram-256gb-storage-2019-model-refurbished-grade-a/15265626?icmp=Recos_3across_tp_sllng_prdcts&referrer=PLP_Reco')


print(driver.title)

isComplete = False

while not isComplete:
  try:
    # wait for add to cart button 
    atcBtn = WebDriverWait(driver,10).until(
      EC.element_to_be_clickable((By.CSS_SELECTOR,'#test > button'))
    )
    isComplete = True;
    print("button is clickable")

    atcBtn.click()
  except:
    # refresh the browser 
    # driver.refresh()
    print("except")
    continue

  try:

    time.sleep(2)
    # wait for view cart button
    gtcBtn = WebDriverWait(driver,10).until( 
      EC.presence_of_element_located((By.CSS_SELECTOR, '#cartIcon > div.confirmation_2-j2W > div > div > div > section > div > button > span'))
    )
    gtcBtn.click()
    
    time.sleep(4)
    # wait for checkout button
    checkoutBtn = WebDriverWait(driver,10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR,'#root > div > div.pageContent_1vNlW > div.loader_3thnw > div.loadedContent_2Wp84 > section > div > main > section > section.cost-sum-section_3pPEp > div:nth-child(3) > div > a > span'))
    )
    checkoutBtn.click()

    time.sleep(1)
    # wait for checkout as guest button
    guestBtn = WebDriverWait(driver,10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR,'#root > div > div.other-context-sign-in-page-content-container > div > div > div > div.VyTnq._1tm4U.h8UpA._24uQr > div > div.guest-continue-link-wrapper > a > span'))
    )
    guestBtn.click()

    print("email input...")
    #fill in information on shipping form
    # select the form items and add info to them by using element.sendKeys("data to insert into form")

    time.sleep(3)

    emailInput = WebDriverWait(driver,10).until(
      EC.presence_of_element_located((By.ID,'email'))
    )
      
    emailInput.send_keys("test@gmail.com")

    # email
    # firstname lastname
    # addresss
    # city
    # province
    # postal Code
    # country
    # phone number
  
    # after info is filled out, press the continue button

    # continueBtn= WebDriverWait(driver,10).until(
    #   EC.presence_of_element_located((By.CSS_SELECTOR,'#posElement > section > section.cost-sum-section > button > span'))
    # )

    # continueBtn.click()

    # fill in credit card information


    # click the continue button again 


  except:
    print("what")
    continue














