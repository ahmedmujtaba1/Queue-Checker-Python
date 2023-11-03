import urllib.request
import random
username = 'themostpolenta'
password = 'FiverPass1'
country = 'DE'
entry = "http://customer-themostpolenta-sessid-0457818374-sesstime-10:FiverPass1@pr.oxylabs.io:7777"
query = urllib.request.ProxyHandler({
    'http': entry,
    'https': entry,
})
execute = urllib.request.build_opener(query)
print(execute.open('https://ip.oxylabs.io').read())

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f'--proxy-server=pr.oxylabs.io:7777')
# driver = webdriver.Chrome(options=chrome_options)
# #add argument with proxy infos
# driver.get("https://customer-themostpolenta:FiverPass1@pr.oxylabs.io:7777")
# driver.get('https://myexternalip.com/raw')
# time.sleep(10000)
# driver.quit()