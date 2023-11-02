import re, undetected_chromedriver as uc
from typing import Optional
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def chrome_proxy(user: str, password: str, endpoint: str) -> dict:
    wire_options = {
        "proxy" : ""
    } 