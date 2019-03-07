#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 18:26
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : jd.py

# -*- coding:utf-8 -*-

from selenium import webdriver
import datetime
import time

driver = webdriver.Chrome()
# https://cart.jd.com/tproduct?pid=7437788&rid=0.2424729128114953

#http://gate.jd.com/InitCart.aspx?pid=100000400010&pcount=1&ptype=1

def login(username, password):
    driver.get("https://passport.jd.com/new/login.aspx")
    time.sleep(1)
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_name("loginname").send_keys(username)
    driver.find_element_by_name("nloginpwd").send_keys(password)
    driver.find_element_by_id("loginsubmit").click()
    time.sleep(1)
    driver.get("https://cart.jd.com/cart.action")
    time.sleep(1)

    # if driver.find_element_by_link_text("去结算"):
    #     driver.find_element_by_link_text("去结算").click()

    now = datetime.datetime.now()
    #now_time = now.strftime('%Y-%m-%d %H:%M:%S')
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    print('login success, you can ou up!')

def buy_on_time(buytime):
    while True:
        # driver.get("http://gate.jd.com/InitCart.aspx?pid=7437708&pcount=1&ptype=1")
        now = datetime.datetime.now()
        print(now.strftime('%Y-%m-%d %H:%M:%S'))
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            print('click!')
            driver.get("http://gate.jd.com/InitCart.aspx?pid=7437708&pcount=1&ptype=1")
            # driver.find_element_by_id('order-submit').click()
            # time.sleep(2)
            print(now.strftime('%Y-%m-%d %H:%M:%S'))
            print('purchase success')
        time.sleep(0.5)

login('18615214533', 'Lh19960405')
buy_on_time('2019-03-05 10:11:40')