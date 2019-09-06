from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session, jsonify
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_binary
#from webdrClass import Webdriver
#import pesqCxaqui
import pandas as pd
#from pathlib import Path
#from flask_session import Session
import os
from datetime import datetime
import threading
import sys
import logging
from shutil import copyfile
import time
import subprocess
from PIL import Image

DRIVER = 'CHROME'
SENHACXAQUI = "1234"

app = Flask(__name__)

@main.route('/')
def index():
    response = principal()
    return "initial" + str(response)

def principal():
  driverCxaqui = criaDriver()
  retorno = loginCxaqui(driverCxaqui)
  print (retorno)
  print("end")

def criaDriver():
  print("em cria Driver")
  if DRIVER =='CHROME':
     options = Options()
     chrome_options = webdriver.ChromeOptions()
     #chrome_options.add_argument('--kiosk-printing')
     chrome_options.add_argument('--no-sandbox')
     chrome_options.add_argument('--headless')
     options.add_argument("--disable-dev-shm-usage")
     options.add_argument("--disable-extensions")
     options.add_argument("start-maximized")
     options.add_argument("disable-infobars")
     #options.headless = True
     #webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
     driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)
     print("escolhido driver Chrome")
     options = Options()
     myProxy = "10.0.x.x:yyyy"
     options.add_argument('--proxy-server=%s' % myProxy)

     from pyvirtualdisplay import Display
     display = Display(visible=0, size=(1024, 768))
     display.start()

     driver = webdriver.Chrome('/usr/bin/chromedriver',options=options, service_args=['--verbose', '--log-path=/home/ubuntu/log/chromedr.log'])
     print(driver.title)

  elif DRIVER == 'PHANTOMJS':
     driver = webdriver.PhantomJS('/usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs',service_args=['--ssl-protocol=any'])
     print("escolhido driver PhantomJS")
  elif DRIVER == 'FIREFOX':
     driver = webdriver.Firefox()
     print("escolhido driver Firefox")
  else:
     driver = webdriver.PhantomJS() #webdriver.
     print("escolhido driver PhantomJS")
  return driver
  
def loginCxaqui(driver):
  try:
    print("login cx aqui")
    driver.get("https://www.caixaqui.gov.br")
    print("driver.get cxaqui")
    driver.implicitly_wait
    time.sleep(5)

    html = driver.page_source
    #print(html)
    filename = "arquivoCXAquihtml"
    arquivo = open(filename, "w+")
    arquivo.write(arquivo)
    arquivo.close()

    driver.implicitly_wait
    elem = driver.find_element_by_name("convenio")
    print("apos find.elem.convenio")
    elem.clear()
    elem.send_keys("000450001")
    print("driver find convenio após sendkeys")
    elem = driver.find_element_by_name("login")
    elem.clear()
    elem.send_keys("usuario")
    
    elem = driver.find_element_by_name("password")
    elem.clear()
    elem.send_keys(SENHACXAQUI)

    driver.implicitly_wait
    print("before btn click")
    driver.find_element_by_class_name("btn-azul").click()

    html = driver.page_source
    resp1 = html.find("000")
    print(html)

    if (resp1 > 0):
        retorno = True
    else:
        retorno = False

    return retorno
  except:
    print("erro no login")
   
if __name__=="__main__":
  app.run(threaded=True)
  app.debug = True
  #main()

