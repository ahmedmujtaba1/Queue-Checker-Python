import selenium, undetected_chromedriver as uc, time, csv, os, configparser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from twocaptcha import TwoCaptcha

chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-infobars')

url = 'https://dfentertainment.queue-it.net/softblock/?c=dfentertainment&e=redhotconcertweek&cid=es-CL&rticr=0'
driver = uc.Chrome(options=chrome_options, version_main=118)
driver.get(url)
time.sleep(2)
wait = WebDriverWait(driver, 5)
config = configparser.ConfigParser()
config.read('setup.ini')
two_captcha_api = config.get("admin","2captcha_api_key")
captcha_image = wait.until(EC.presence_of_element_located((By.XPATH,"//img[@class='captcha-code']")))
captcha_image.screenshot('captchas/captcha.png')
solver = TwoCaptcha(apiKey=two_captcha_api)
try:
    result = solver.normal('captchas/captcha.png')
except Exception as ex:
    print("Error : ", ex)
time.sleep(22222)