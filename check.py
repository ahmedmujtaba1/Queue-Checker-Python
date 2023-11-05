from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from twocaptcha import TwoCaptcha
import configparser, time, csv

USERNAME = "themostpolenta"
PASSWORD = "FiverPass1"
ENDPOINT = "pr.oxylabs.io:7777"

with open('output/output.csv', 'w', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['URL', 'Identifacador de fila', 'última actualización'])

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
                solver = TwoCaptcha(apiKey=two_captcha_api)
                try:
                    result = solver.normal('captchas/captcha.png')
                except Exception as ex:
                    print("Error : ", ex)

                else: 
                    code = result['code']
                    print("[+] Captcha Code : ",code)
                    captcha_input_container = driver.find_element(By.ID,"solution")
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
                        wait.until(EC.presence_of_element_located((By.ID,"MainPart_divProgressbar")))
                        time.sleep(4)
                        wait = WebDriverWait(driver, 25)
                        time2 = driver.find_element(By.ID,"MainPart_lbLastUpdateTimeText").text
                        time.sleep(1)
                        flag2 = True
                        while flag2:
                            try:
                                wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='RED HOT CHILI PEPPERS']")))
                                break
                            except:
                                time.sleep(1)
                        time.sleep(0.4)
                        current_url = driver.current_url
                        print("Token URL : ", current_url, " Estimated Time : ", time2)
                        with open('output/output.csv', 'a', encoding="utf-8") as f:
                            writer = csv.writer(f)
                            writer.writerow(['URL', 'Identifacador de fila', 'última actualización'])
                        flag = False
                        break
                    # time.sleep(22222)
    finally:
        driver.quit()


if __name__ == "__main__":
    run = int(input("[+] How many times you want to run the bot : "))
    print(execute_driver(run))