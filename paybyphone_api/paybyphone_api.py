import chromedriver_autoinstaller

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

chromedriver_autoinstaller.install(cwd=True)


def open_action(country_code, timeout=10, headless=True):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)

    driver.delete_all_cookies()

    driver.get('https://m2.paybyphone.fr/login')

    country_panel = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//div[@role="presentation"]')))

    WebDriverWait(country_panel, timeout).until(EC.presence_of_element_located((By.XPATH, f'//input[@value="{country_code}"]'))).click()
    WebDriverWait(country_panel, timeout).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Select"]'))).click()
    return driver


def login_action(driver, num, password, timeout=10):
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.NAME, "phoneLogin"))).send_keys(num)
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys(password + Keys.RETURN)

    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Agree & Continue']"))).click()
    finally:
        return driver


def topup_action(driver, location, time, unit, timeout=10):

    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Park']"))).click()
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.NAME, "advertisedLocationNumber"))).send_keys(location + Keys.RETURN)

    while len(driver.find_elements_by_tag_name('md-option')) == 0:
        sleep(1)

    units_elements = driver.find_elements_by_tag_name('md-option')

    units = [element.get_attribute('analytics-label').lower() for element in units_elements]

    if unit.lower() not in units:
        return "Failed", f'{unit} is not a supported unit (available : {units}'
    else:
        if len(units) > 1:
            WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.CLASS_NAME, 'md-select-icon'))).click()
            WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, f'//md-option[@analytics-label="{unit.lower()}"]'))).click()

    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.NAME, "quantity"))).send_keys(str(time) + Keys.RETURN)

    amount = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//p[text()="Total charges"]/following-sibling::h4'))).text

    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    WebDriverWait(driver, timeout + 10).until(
        EC.presence_of_element_located((By.XPATH, '//h1[contains(text(),"paid")]')))

    driver.close()

    return "Success", amount


def topup(country_code, num, password, location, time, unit, timeout=10, headless=True):
    driver = open_action(country_code, headless=headless, timeout=timeout)
    login_action(driver, num, password, timeout=timeout)
    sleep(5)
    topup_action(driver, location, time, unit, timeout=timeout)


print(topup("FR", "+33664636501", "003614", "75017", "1", "minutes", headless=False))
