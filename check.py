import re
from typing import Optional

from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
# A package to have a chromedriver always up-to-date.
from webdriver_manager.chrome import ChromeDriverManager

USERNAME = "your_username"
PASSWORD = "your_password"
ENDPOINT = "pr.oxylabs.io:7777"


def chrome_proxy(user: str, password: str, endpoint: str) -> dict:
    wire_options = {
        "proxy": {
            "http": f"http://{user}:{password}@{endpoint}",
            "https": f"http://{user}:{password}@{endpoint}",
        }
    }

    return wire_options


def get_ip_via_chrome():
    manage_driver = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.headless = True
    proxies = chrome_proxy(USERNAME, PASSWORD, ENDPOINT)
    driver = webdriver.Chrome(
        service=manage_driver, options=options, seleniumwire_options=proxies
    )
    try:
        driver.get("https://ip.oxylabs.io/")
        return f'\nYour IP is: {re.search(r"[0-9].{2,}", driver.page_source).group()}'
    finally:
        driver.quit()


if __name__ == "__main__":
    print(get_ip_via_chrome())
