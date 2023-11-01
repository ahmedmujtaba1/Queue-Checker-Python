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
# chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-infobars')

url = 'https://dfentertainment.queue-it.net/softblock/?c=dfentertainment&e=redhotconcertweek&cid=es-CL&rticr=0'
driver = uc.Chrome(options=chrome_options, version_main=118)
driver.maximize_window()
driver.get(url)
time.sleep(2)
wait = WebDriverWait(driver, 5)
config = configparser.ConfigParser()
config.read('setup.ini')
two_captcha_api = config.get("admin","2captcha_api_key")
captcha_image = wait.until(EC.presence_of_element_located((By.XPATH,"//img[@class='captcha-code']")))
captcha_image.screenshot('captchas/captcha.png')
driver.find_element(By.ID,"playAudio").click()
solver = TwoCaptcha(apiKey=two_captcha_api)
try:
    result = solver.normal('captchas/captcha.png')
except Exception as ex:
    print("Error : ", ex)

else: 
    code = result['code']
    print("[+] Captcha Code : ",code)
    captcha_input_container = driver.find_element(By.ID,"solution")
    captcha_input_container.click()
    for i in range(len(str(code))):
        # captcha_input_container.send_keys(code)
        captcha_input_container.send_keys(code[i])
        time.sleep(0.3)
    time.sleep(1.2)
    driver.find_element(By.XPATH,"//div[@id='challenge-container']//button").click()
time.sleep(22222)