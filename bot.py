import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import random
import info

def getRand():
  randNum = random.randint(1,4)
  return randNum 

# TODO: add threading for the form inputs
def bestbuy():

  # options = uc.ChromeOptions()
  # options.add_experimental_option('exclueSwitches', ["enabled-logging"])
  driver = uc.Chrome()
  # driver.get('https://www.bestbuy.ca/en-ca/product/apple-macbook-air-13-1-6ghz-intel-core-i5-8gb-ram-256gb-storage-2019-model-refurbished-grade-a/15265626?icmp=Recos_3across_tp_sllng_prdcts&referrer=PLP_Reco')
  driver.get('https://www.bestbuy.ca/en-ca/product/apple-61w-usb-c-power-adapter-mrw22ll-a/13234006?icmp=Recos_4across_y_mght_ls_lk')

  isComplete = False

  while not isComplete:
    try:
      # wait for add to cart button to be clickable
      atcBtn = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'#test > button'))
      )
      isComplete = True;
      print("ATC button is clickable")
      atcBtn.click()
    except:
      # refresh the browser every 10s until the atc btn is clickable
      time.sleep(10)
      driver.refresh()
      print("ATC button not avaliable.")
      print("Refreshing page...")
      continue

    try:
      # wait for view cart button
      time.sleep(getRand())
      # time.sleep(4)
      gtcBtn = WebDriverWait(driver,10).until( 
        EC.presence_of_element_located((By.CSS_SELECTOR, '#cartIcon > div.confirmation_2-j2W > div > div > div > section > div > button > span'))
      )
      gtcBtn.click()
      
      # wait for checkout button
      time.sleep(getRand())
      # time.sleep(3)
      checkoutBtn = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#root > div > div.pageContent_1vNlW > div.loader_3thnw > div.loadedContent_2Wp84 > section > div > main > section > section.cost-sum-section_3pPEp > div:nth-child(3) > div > a > span'))
      )
      checkoutBtn.click()

      # wait for checkout as guest button
      time.sleep(getRand())
      guestBtn = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#root > div > div.other-context-sign-in-page-content-container > div > div > div > div.VyTnq._1tm4U.h8UpA._24uQr > div > div.guest-continue-link-wrapper > a > span'))
      )
      guestBtn.click()

      print("Completing shipping form...")
      #fill in information on shipping form
      # select the form items and add info to them by using element.sendKeys("info to insert into form")
      emailInput = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'email'))
      )
      emailInput.send_keys(info.email)

      firstNameInput = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'firstName'))
      )
      
      firstNameInput.send_keys(info.firstName)

      lastNameInput = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'lastName'))
      )

      lastNameInput.send_keys(info.lastName)

      addressInput = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'addressLine'))
      )

      addressInput.send_keys(info.address)

      cityInput = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'city'))
      )

      cityInput.send_keys(info.city)

      # province
      provinceInput = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'regionCode'))
      )

      provinceOptions = provinceInput.find_elements_by_tag_name('option')
      for option in provinceOptions:
        if option.get_attribute("value") == info.province:
          option.click()
          break

      postalCodeInput = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'postalCode'))
      )

      postalCodeInput.send_keys(info.postalCode)

      phoneInput = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'phone'))
      )

      phoneInput.send_keys(info.phoneNumber)
    
      # after info is filled out, press the continue button
      time.sleep(getRand())
      continueBtn= WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#posElement > section > section.cost-sum-section > button > span'))
      )

      continueBtn.click()

      print("Completing cc form")
      # fill in credit card information
      ccInput = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'shownCardNumber'))
      )

      # add credit card info to make a test purchase 
      ccInput.send_keys(info.ccNum)

      expMonthInput = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'expirationMonth'))
      )

      expMonthOptions = expMonthInput.find_elements_by_tag_name('option')
      for option in expMonthOptions:
        if option.get_attribute("value") == info.expMonth:
          option.click()
          break
        
      expYearInput = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'expirationYear'))
      )

      expYearOptions = expYearInput.find_elements_by_tag_name('option')

      for option in expYearOptions:
        if option.get_attribute("value") == info.expYear: 
          option.click()
          break
        
      cvvInput = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'cvv'))
      )

      cvvInput.send_keys(info.ccv)

      print("horraaayyy")

      # place order button

      placeOrderInput = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#posElement > section > section.cost-sum-section > button > span'))
      )

      # TODO: uncomment this when you're ready to test a real purchase
      # placeOrderInput.click()
  
      # click the continue button again 

      # exit loop
      isComplete = True
      driver.quit()
      return isComplete

    except Exception as e:
      print("error :( ", e)
      isComplete = False
      driver.quit()
      return isComplete

def main():
  # run this function until we get return true
  print("calling best buy function...")

  attempt = bestbuy()

  i = 0
  while not attempt:
    print("attempt #", i)
    attempt = bestbuy()
    print("Did it work?")
    print(attempt)
    i = i + 1

if __name__ == "__main__":
  main()







