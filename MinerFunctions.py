#!/usr/bin/env python

import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import array
import time
import string
import CaCClass

with open("config.json") as config_file:
    config = json.load(config_file)

def GetBitcoinPrice():
    JsonResponse = json.loads((requests.get("https://blockchain.info/ticker")).text)
    return (JsonResponse['USD']['sell'])

def GetWalletInfoCaCPanel():
    FireFoxOptions = webdriver.FirefoxOptions()
    FireFoxOptions.set_headless()
    driver = webdriver.Firefox(executable_path='./modules/geckodriver-v0.29.0-win64/geckodriver',firefox_options=FireFoxOptions) 
    driver.get("https://panel.cloudatcost.com/login.php")
    UserElem = driver.find_element_by_name("username")
    UserElem.send_keys(config['credentials']['user'])
    PasswordElem = driver.find_element_by_name("password")
    PasswordElem.send_keys(config['credentials']['passwd'])
    SubmitButton = driver.find_element_by_xpath('//*[@id="login-form"]/input[4]')
    SubmitButton.click()
    driver.get("https://panel.cloudatcost.com/wallet")
    WalletInfo = (driver.find_element_by_xpath('//*[@id="dataTable"]/tbody')).text
    driver.close()
    array = []
    linesplit = WalletInfo.splitlines()
    for line in linesplit:
        templine = line.split(" ")
        tempObj = CaCClass.WalletLine(templine[0],templine[1],templine[2],templine[4],templine[5],templine[7])
        array.append(tempObj)
    return array

def UniqueMinerNumbers(WalletArray):
    UniqueMiners = []
    for object in WalletArray:
        if object.MinerID not in UniqueMiners:
            UniqueMiners.append(object.MinerID)
    return UniqueMiners

def SummaryCaCMinerInfo(MinerNumber,WalletArray):
    SumOfBTC = 0
    for object in WalletArray:
        if object.MinerID == MinerNumber:
            SumOfBTC += float(object.Amount)
    return SumOfBTC

def GetBTCValue(BTCAmount):
    CurrentBTCValue = GetBitcoinPrice()
    DollarValue = (CurrentBTCValue * BTCAmount)
    return DollarValue

def PostToCloudatCocksSite():
    FireFoxOptions = webdriver.FirefoxOptions()
    FireFoxOptions.set_headless()
    driver = webdriver.Firefox(executable_path='./modules/geckodriver-v0.29.0-win64/geckodriver',firefox_options=FireFoxOptions) 
    driver.get("https://panel.cloudatcost.com/login.php")
    UserElem = driver.find_element_by_name("username")
    UserElem.send_keys(config['credentials']['user'])
    PasswordElem = driver.find_element_by_name("password")
    PasswordElem.send_keys(config['credentials']['passwd'])
    SubmitButton = driver.find_element_by_xpath('//*[@id="login-form"]/input[4]')
    SubmitButton.click()
    driver.get("https://panel.cloudatcost.com/wallet")
    WalletInfo = (driver.find_element_by_xpath('//*[@id="dataTable"]/tbody')).text
    driver.close()

    TabStringWalletInfo = ""
    linesplit = WalletInfo.splitlines()
    for line in linesplit:
        templine = line.split(" ")
        tempObj = templine[0]+'\t'+templine[1]+'\t'+templine[2]+' '+templine[3]+'\t'+templine[4]+'\t'+templine[5]+' '+templine[6]+'\t'+templine[7]+'\n'
        TabStringWalletInfo = TabStringWalletInfo + tempObj

    driver = webdriver.Firefox(executable_path='./modules/geckodriver-v0.29.0-win64/geckodriver',firefox_options=FireFoxOptions) 
    driver.get("https://mining.cloudatcocks.com/login")
    UserElem = driver.find_element_by_xpath('//*[@id="email"]')
    UserElem.send_keys(config['cloudatcockscredentials']['user'])
    PasswordElem = driver.find_element_by_xpath('//*[@id="password"]')
    PasswordElem.send_keys(config['cloudatcockscredentials']['passwd'])
    LoginElem = driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[4]/button')
    LoginElem.click()
    time.sleep(5)
    driver.get("https://mining.cloudatcocks.com/payouts/create")
    SubmitElem = driver.find_element_by_xpath('//*[@id="details"]')
    SubmitElem.send_keys(TabStringWalletInfo)
    SubmitButton = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/main/div/div/main/div/div/div[2]/table/tfoot/tr/td/button')
    SubmitButton.click()
    time.sleep(10)
    driver.close()