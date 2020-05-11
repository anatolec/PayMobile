from selenium import webdriver
import time

def topup(num, password, cp, days=6):
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)

    driver.get('https://m2.paybyphone.fr/login')

    driver.implicitly_wait(100)
    driver.find_element_by_name('phone').send_keys(num)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_xpath("//button[@type='submit']").click()

    time.sleep(5)

    els = driver.find_elements_by_xpath("//button[@analytics-event='Accept GDPR']")

    if len(els):
        els[0].click()

    time.sleep(5)

    driver.find_element_by_xpath("//span[text()='Stationner']").click()

    time.sleep(5)

    driver.find_element_by_name('advertisedLocationNumber').send_keys(cp)
    driver.find_element_by_xpath("//span[text()='Continuer']").click()

    time.sleep(5)

    driver.find_element_by_name('quantity').send_keys(days)
    driver.find_element_by_xpath("//span[text()='Continuer']").click()

    time.sleep(5)

    driver.find_element_by_xpath("//button[@type='submit']").click()

    time.sleep(20)

    driver.close()
