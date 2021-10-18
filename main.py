"""
"""
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def login(driver: webdriver, usuario, senha) -> None:
    print("»»» Loguin em andamento")
    var = None
    driver.get("https://www.bet365.com/#/HO/")
    driver.set_page_load_timeout(10)
    sleep(2)
    elem = driver.find_elements(By.TAG_NAME, "div")
    for el in elem:
        if el.text == "Login":
            var = el
            break
    var.click()
    elem = driver.find_elements(By.TAG_NAME ,"input")
    for el in elem:
        if el.get_attribute("placeholder") == "Usuário":
            var = el
            el.send_keys(usuario)
            break
    for el in elem:
        if el.get_attribute("placeholder") == "Senha":
            el.send_keys(senha)
            break
    elem = driver.find_element(By.CLASS_NAME ,"lms-StandardLogin_LoginButton ")
    elem.click()
   
def to_check_loguin(driver: webdriver, user) -> bool:
    sleep(3)
    check = False
    compare = driver.find_elements(By.ID, "body > div:nth-child(1) > div > div.wc-WebConsoleModule_SiteContainer > div.wc-WebConsoleModule_Header > div > div:nth-child(1) > div > div > div.um-Header > div.um-Header_InfoRow > div.um-Header_LeftSideWrapper > div > div > span.um-UserInfo_UserName")
    for ele in compare:
        if ele.text == user:
            print(ele.text)
            print(True)
            check = True
    return check
    
def painel():
    menu = """"
 MENU
 1.
 2.
 3.
 4.
"""

os.system("clear")
user = input("Nome de Usuário: ")
password = input("Senha: ")
with webdriver.Firefox() as driver:
    login(driver, user, password)
    to_check_loguin(driver, user)
    #os.system("clear")
    print("entrando...")
    while (painel := input(f"{menu}\n»»» ") != "0"):
        ...