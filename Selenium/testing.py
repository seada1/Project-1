from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class navigator:
    serv = Service(
        "C:/Users/Owner/Downloads/chromedriver")
    driver: WebDriver = webdriver.Chrome(service=serv)

    @classmethod
    def form(cls):
        return cls.driver.find_element(by=By.ID, value="login")

    @classmethod
    def clicking(cls):
        while (True):
            cls.form().click()


def main():
    navigator.driver.get("http://127.0.0.1:5501/TRMS/index.html")
    sleep(1)
    navigator.driver.get("http://127.0.0.1:5501/TRMS/login.html")
    sleep(1)
    navigator.driver.get("http://127.0.0.1:5501/TRMS/form.html")
    sleep(1)
    navigator.clicking()
    navigator.driver.quit()


if __name__ == '__main__':
    main()
