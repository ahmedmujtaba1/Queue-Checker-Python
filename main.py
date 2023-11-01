import selenium, undetected_chromedriver as uc, time, csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-infobars')

url = 'https://dfentertainment.queue-it.net/softblock/?c=dfentertainment&e=redhotconcertweek&cid=es-CL&rticr=0'
driver = uc.Chrome(options=chrome_options)
driver.get(url)
time.sleep(22222)