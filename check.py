# import urllib.request
# import random
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time


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

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument(f'--proxy-server={ip_address}:7777')
# chrome_options.add_argument(f'--proxy-server={ip_address}:7777')
driver = webdriver.Chrome(options=chrome_options)
#add argument with proxy infos
driver.get('https://myexternalip.com/raw')
time.sleep(10000)
driver.quit()