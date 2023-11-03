# import urllib.request
# import random
# username = 'themostpolenta'
# password = 'FiverPass1'
# country = 'DE'
# entry = ('http://customer-%s-cc-%s:%s@pr.oxylabs.io:7777' %
#     (username, country, password))
# query = urllib.request.ProxyHandler({
#     'http': entry,
#     'https': entry,
# })
# execute = urllib.request.build_opener(query)
# print(execute.open('https://ip.oxylabs.io').read())

from selenium import webdriver
from selenium.webdriver.common.by import By