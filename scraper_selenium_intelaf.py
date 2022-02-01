
import re
from webbrowser import Chrome
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


import time

links = ['https://www.intelaf.com/Precios_stock_resultado.aspx?area=COMPU-CASES']

info = []

for i in range (len(links)):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('window-size= 1920x1080')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #driver = webdriver.Chrome(options=chrome_options)
    driver.get(links[i])

    time.sleep(10)
    squadPage = driver.page_source
    soup = BeautifulSoup(squadPage, 'html.parser')
    productos = soup.findAll('div', class_=re.compile('col-xs-12 col-md-6 col-lg-4'))
    print('Productos', len(productos))
    print(productos)

    driver.quit()