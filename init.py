from cgitb import text
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(20)
driver.maximize_window()

def login(email, password, textFile):
    driver.get('https://www.linkedin.com/login/es?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

    emailInput = driver.find_element(By.NAME, 'session_key')
    emailInput.send_keys(email)

    passwordInput = driver.find_element(By.NAME, 'session_password')
    passwordInput.send_keys(password)

    loginButton = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    loginButton.click()

    publishBox = driver.find_element(By.XPATH, '//*[@id="ember37"]')
    publishBox.click()

    postarea = driver.find_element(By.CLASS_NAME, "ql-editor.ql-blank")
    postarea.send_keys(parseText(textFile))
    sleep(1)

    publishButtonContainer = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[3]')
    publishButtonContainer.find_element(By.TAG_NAME, 'button').click()

def parseText(textFile):
    with open(textFile, "r", encoding="utf8")as file:
        readline=file.read().splitlines()
        butFirst = readline[0:]
        eachInASeparateLine = "\n".join(butFirst)
        print(eachInASeparateLine)
        return eachInASeparateLine

if __name__ == "__main__":
    email = sys.argv[1]
    password = sys.argv[2]
    textFile = sys.argv[3]
    login(email, password, textFile)
