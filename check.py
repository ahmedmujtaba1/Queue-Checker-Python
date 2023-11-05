
# username = 'themostpolenta'
# password = 'FiverPass1'
# country = 'DE'
# entry = ('https://customer-%s-cc-%s:%s@pr.oxylabs.io:7777' %
#     (username, country, password))
# query = urllib.request.ProxyHandler({
#     'http': entry,
#     'https': entry,
# })
# execute = urllib.request.build_opener(query)
# ip_address = execute.open(' https://ipinfo.io').read()
# ip_address = str(ip_address).split(',')[0]
# ip_address = str(ip_address).split('"')[3]
# print("Ip Address : ", ip_address)

from selenium.webdriver.common.by import By
from seleniumwire import webdriver
# A package to have a chromedriver always up-to-date.
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from twocaptcha import TwoCaptcha
import configparser, time, pyautogui

USERNAME = "themostpolenta"
PASSWORD = "FiverPass1"
ENDPOINT = "pr.oxylabs.io:7777"


def chrome_proxy(user: str, password: str, endpoint: str) -> dict:
    wire_options = {
        "proxy": {
            "http": f"http://{user}:{password}@{endpoint}",
            "https": f"http://{user}:{password}@{endpoint}",
        }
    }

    return wire_options


def execute_driver(run_time: int):
    options = webdriver.ChromeOptions()
    options.headless = True
    proxies = chrome_proxy(USERNAME, PASSWORD, ENDPOINT)
    # driver = webdriver.Chrome( seleniumwire_options=proxies)
    chrome_options = webdriver.ChromeOptions()
    user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.5735.99 Mobile/15E148 Safari/604.1"
    chrome_options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    try:
        url = 'https://dfentertainment.queue-it.net/softblock/?c=dfentertainment&e=redhotconcertweek&cid=es-CL&rticr=0'
        driver.get(url)
        for i in range(run_time):
            flag = True
            while flag:
                time.sleep(2)
                wait = WebDriverWait(driver, 5)
                config = configparser.ConfigParser()
                config.read('setup.ini')
                two_captcha_api = config.get("admin","2captcha_api_key")
                captcha_image = wait.until(EC.presence_of_element_located((By.XPATH,"//img[@class='captcha-code']")))
                captcha_image.screenshot('captchas/captcha.png')
                driver.find_element(By.TAG_NAME,'body').send_keys(Keys.ARROW_DOWN)
                driver.find_element(By.TAG_NAME,'body').send_keys(Keys.ARROW_DOWN)
                time.sleep(0.2)
                try:
                    button_location = pyautogui.locateOnScreen('img/button.png')
                    button_exact_location = pyautogui.center(button_location)
                    pyautogui.moveTo(button_exact_location)
                except:pass
                solver = TwoCaptcha(apiKey=two_captcha_api)
                try:
                    result = solver.normal('captchas/captcha.png')
                except Exception as ex:
                    print("Error : ", ex)

                else: 
                    code = result['code']
                    print("[+] Captcha Code : ",code)
                    captcha_input_container = driver.find_element(By.ID,"solution")
                    # [captcha_input_container.send_keys(char) for char in str(code).lower()]
                    captcha_input_container.send_keys(code)
                    time.sleep(0.2)
                    captcha_input_container.send_keys(Keys.ENTER)
                    time.sleep(1.2)
                    element_exist = True
                    try:
                        driver.find_element(By.XPATH,"//div[@class='hidden']")
                        element_exist = True
                    except:
                        element_exist = False
                    if not element_exist:
                        flag = False
                        break
                    # time.sleep(22222)
    finally:
        driver.quit()


if __name__ == "__main__":
    run = int(input("[+] How many times you want to run the bot : "))
    print(execute_driver(run))