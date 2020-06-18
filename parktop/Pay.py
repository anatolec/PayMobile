from selenium import webdriver
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()

def topup(num, password, cp, days=6, headless=True):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)

    driver.get('https://m2.paybyphone.fr/login')

    driver.implicitly_wait(100)

    driver.find_element_by_name('phoneLogin').send_keys(num)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_xpath("//button[@type='submit']").click()

    els = driver.find_elements_by_xpath("//button[@analytics-event='Accept GDPR']")

    if len(els):
        time.sleep(1)
        els[0].click()

    driver.find_element_by_xpath("//span[text()='Park']").click()

    driver.find_element_by_name('advertisedLocationNumber').send_keys(cp)
    driver.find_element_by_xpath("//span[text()='Continue']").click()

    driver.find_element_by_name('quantity').send_keys(days)
    time.sleep(1)
    driver.find_element_by_xpath("//span[text()='Continue']").click()

    time.sleep(1)
    driver.find_element_by_xpath("//button[@type='submit']").click()

    driver.close()
