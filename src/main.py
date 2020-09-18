from selenium import webdriver
from config import UERNAME, PASSWORD
import sys

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
    executable_path=r'C:\Users\HAFIS\Desktop\chromedriver_win32\chromedriver'
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

visibility_field = browser.find_element_by_xpath(f'//input[@name="repository[visibility][@value={visibility}]]')
visibility.click()

repo_field.submit()

try:
    copy_btn
except:
    print("can't create repository, try agin")