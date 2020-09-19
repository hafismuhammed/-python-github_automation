from selenium import webdriver
import time
import sys
import pyperclip
from config import USERNAME, PASSWORD

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

try:
    repo_name = sys.argv[1]
except:
    print('Repo name is required')
    sys.exit()

try:
    visibility = sys.argv[2]
except:
    visibility = 'public'

browser = webdriver.Chrome(
    executable_path=r'C:\Users\HAFIS\Desktop\chromedriver_win32\chromedriver', options=chrome_options
)

browser.maximize_window()
browser.get("https://www.github.com/login")

username_field = browser.find_element_by_name('login')
username_field.send_keys(USERNAME)

password_field = browser.find_element_by_name('password')
password_field.send_keys(PASSWORD)

username_field.submit()

browser.get("https://www.github.com/new")

repo_field = browser.find_element_by_name('repository[name]')
repo_field.send_keys(repo_name)

time.sleep(1)

visibility_field = browser.find_element_by_xpath(
    f'//input[@name="repository[visibility]"][@value="{visibility}"]'
    )
visibility_field.click()

repo_field.submit()

try:
    copy_btn = browser.find_element_by_xpath(
        '//clipboard-copy[@for="empty-setup-push-repo-echo"]'
        )
    copy_btn.click()

    #print(pyperclip.paste())
    print(f'git remote add origin https://github.com/hafismuhammed/{repo_name}.git')
    print('git branch -M master')
    print('git push -u origin master')
except:
    print("can't create repository, try agin")