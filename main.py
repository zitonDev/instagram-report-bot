# Stream Point Bot v0.1
# Made by Erv
import time
import os
from selenium import webdriver, common
import Selenium2Library
from colorama import Fore, Back, Style
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("IRB - V1 - By Erv")

status = Fore.RED + "De-Activated" + Style.RESET_ALL
account = Fore.RED + "N/A" + Style.RESET_ALL
rpc = 0

def header():
    os.system('cls')
    print(Style.RESET_ALL + " ▄█     ▄████████ ▀█████████▄  ")
    print("███    ███    ███   ███    ███ ")
    print("███▌   ███    ███   ███    ███ ")
    print("███▌  ▄███▄▄▄▄██▀  ▄███▄▄▄██▀  ")
    print("███▌ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀██▄  ")
    print("███  ▀███████████   ███    ██▄ ")
    print("███    ███    ███   ███    ███ ")
    print("█▀     ███    ███ ▄█████████▀  ")
    print("       ███    ███              ")
    print(Style.RESET_ALL + "────────────────────────────────────────")
    print("IG Report Bot: " + status)
    print("Account: " + account + "  Report Count: " + str(rpc))
    print(Style.RESET_ALL + "────────────────────────────────────────")

header()
print(Fore.GREEN + "Starting Instagram report bot...")
time.sleep(3)

def bot():
    print("Reporting " + Fore.GREEN + "@" + Fore.GREEN + account + Style.RESET_ALL + " with a delay of " + Fore.RED + str(delay) + Style.RESET_ALL + " seconds.")
    time.sleep(3)
    global rpc
    rpc = 0
    global status
    status = Fore.GREEN + "Activated" + Style.RESET_ALL
    while True:
        header()
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
        time.sleep(4)
        driver.close()
        rpc += 1
        time.sleep(delay)

def start():
    header()
    global account
    account = input("IG Username: ")
    global fn
    fn = input("Full Name of User: ")
    global delay
    delay = int(input("Delay between Reports (Seconds): "))
    bot()


if __name__ == '__main__':
    start()
