# import re
# from typing import Optional

# from seleniumwire import webdriver
# from selenium.webdriver.chrome.service import Service
# # A package to have a chromedriver always up-to-date.
# from webdriver_manager.chrome import ChromeDriverManager

# USERNAME = ""
# PASSWORD = ""
# ENDPOINT = "pr.oxylabs.io:7777"


# def chrome_proxy(user: str, password: str, endpoint: str) -> dict:
#     wire_options = {
#         "proxy": {
#             "http": f"http://{user}:{password}@{endpoint}",
#             "https": f"https://customer-themostpolenta-sessid-0637001499-sesstime-10:FiverPass2@pr.oxylabs.io:7777",
#         }
#     }

#     return wire_options


# def get_ip_via_chrome():
#     coptions = webdriver.ChromeOptions()
#     coptions.headless = True
#     proxies = chrome_proxy(USERNAME, PASSWORD, ENDPOINT)
#     driver = webdriver.Chrome(ChromeDriverManager().install(), options=coptions, seleniumwire_options=proxies)
#     try:
#         driver.get("https://ip.oxylobs.io/")
#         return driver.page_source
#     finally:
#         driver.quit()

# print(get_ip_via_chrome())


# if __name__ == "__main__":
#     print(get_ip_via_chrome())

from selenium import webdriver
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('')
# chrome_options.add_argument(f'--proxy-server={proxy_ip_port}')
driver = webdriver.Chrome(options=chrome_options)

driver.get('http://whatismyipaddress.com')

time.sleep(8)

driver.quit()