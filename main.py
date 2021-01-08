import time
import os
from selenium import webdriver, common
import ctypes
from _thread import *


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = "\033[;0m"
    RED = "\033[;31m"

#Title
ctypes.windll.kernel32.SetConsoleTitleW("IRB - V1 - By Erv")

#Variables
account = ""
fn = ""
rpc = 1
delay = 0


def c1header(work):
    if work == True:
        global account
        global fn
        global delay
        global rpc
        os.system("cls")

        print(
            f"            {bcolors.OKBLUE}██{bcolors.RED}╗{bcolors.OKBLUE}██████{bcolors.RED}╗ {bcolors.OKBLUE}██████{bcolors.RED}╗ ")
        print(
            f"            {bcolors.OKBLUE}██{bcolors.RED}║{bcolors.OKBLUE}██{bcolors.RED}╔══{bcolors.OKBLUE}██{bcolors.RED}╗{bcolors.OKBLUE}██{bcolors.RED}╔══{bcolors.OKBLUE}██{bcolors.RED}╗")
        print(
            f"            {bcolors.OKBLUE}██{bcolors.RED}║{bcolors.OKBLUE}██████{bcolors.RED}╔╝{bcolors.OKBLUE}██████{bcolors.RED}╔╝")
        print(
            f"            {bcolors.OKBLUE}██{bcolors.RED}║{bcolors.OKBLUE}██{bcolors.RED}╔══{bcolors.OKBLUE}██{bcolors.RED}╗{bcolors.OKBLUE}██{bcolors.RED}╔══{bcolors.OKBLUE}██{bcolors.RED}╗")
        print(
            f"            {bcolors.OKBLUE}██{bcolors.RED}║{bcolors.OKBLUE}██{bcolors.RED}║  {bcolors.OKBLUE}██{bcolors.RED}║{bcolors.OKBLUE}██████{bcolors.RED}╔╝")
        print(f"            {bcolors.RED}╚═╝╚═╝  ╚═╝╚═════╝ {bcolors.RESET}")
        account = input(f"Account: _> ")
        fn = input(f"Full Name: _> ")
        delay = input(f"Delay (Seconds): _> ")

def bot(showheader):


    global account
    global fn
    global testing
    time.sleep(3)
    global rpc



    while True:
        if showheader == True:

            ctypes.windll.kernel32.SetConsoleTitleW(f"IRB - Reports [{rpc}]")
            os.system("cls")
            print(
                f"            {bcolors.OKBLUE}██{bcolors.RED}╗{bcolors.OKBLUE}██████{bcolors.RED}╗ {bcolors.OKBLUE}██████{bcolors.RED}╗ ")
            print(
                f"            {bcolors.OKBLUE}██{bcolors.RED}║{bcolors.OKBLUE}██{bcolors.RED}╔══{bcolors.OKBLUE}██{bcolors.RED}╗{bcolors.OKBLUE}██{bcolors.RED}╔══{bcolors.OKBLUE}██{bcolors.RED}╗")
            print(
                f"            {bcolors.OKBLUE}██{bcolors.RED}║{bcolors.OKBLUE}██████{bcolors.RED}╔╝{bcolors.OKBLUE}██████{bcolors.RED}╔╝")
            print(
                f"            {bcolors.OKBLUE}██{bcolors.RED}║{bcolors.OKBLUE}██{bcolors.RED}╔══{bcolors.OKBLUE}██{bcolors.RED}╗{bcolors.OKBLUE}██{bcolors.RED}╔══{bcolors.OKBLUE}██{bcolors.RED}╗")
            print(
                f"            {bcolors.OKBLUE}██{bcolors.RED}║{bcolors.OKBLUE}██{bcolors.RED}║  {bcolors.OKBLUE}██{bcolors.RED}║{bcolors.OKBLUE}██████{bcolors.RED}╔╝")
            print(f"            {bcolors.RED}╚═╝╚═╝  ╚═╝╚═════╝ {bcolors.RESET}")
            print(f"           Instagram Account: {account}")
            print(f"           Reports: {rpc}")

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disables logging
        options.add_argument('--disable-extensions')
        options.add_argument('--profile-directory=Default')
        options.add_argument("--incognito")
        options.add_argument("--disable-plugins-discovery");
        options.add_argument("--headless") # Turns Chrome into headless browser
        options.add_argument("--mute-audio")
        driver = webdriver.Chrome(options=options)
        driver.get('https://help.instagram.com/contact/723586364339719')
        driver.find_element_by_xpath('//input[@name="Field258021274378282"]').send_keys(account)
        driver.find_element_by_xpath('//input[@name="Field735407019826414"]').send_keys(fn)
        driver.find_element_by_xpath('//span[@class="_55pe"]').click()
        driver.find_element_by_xpath('//ul[@class="_54nf"]//a[@title="2009"]').click()
        driver.find_element_by_xpath('//a[@class="_p _55pi _5vto _55_p _2agf _4o_4 _4jy0 _4jy3 _517h _51sy _42ft"]//span[@class="_55pe"]').click()
        driver.find_element_by_xpath('//a[@title="August"]//span[@class="_54nh"]').click()
        driver.find_element_by_xpath('//a[@class="_p _55pi _5vto _55_p _2agf _4o_4 _4jy0 _4jy3 _517h _51sy _42ft"]//span[@class="_55pe"]').click()
        driver.find_element_by_xpath('//a[@title="11"]//span[@class="_54nh"]').click()
        driver.find_element_by_xpath('//select[@id="294540267362199"]//option[@value="Other"]').click()
        driver.find_element_by_xpath('//button[@class="_42ft _4jy0 _4jy4 _4jy1 selected _51sy"]').click()
        time.sleep(3)
        driver.close()
        rpc += 1
        time.sleep(int(delay))

def start():
    global testing
    c1header(True)
    # (False) later for multithreading
    start_new_thread(bot(True))

if __name__ == '__main__':
    start()