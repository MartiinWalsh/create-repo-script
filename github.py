import os, sys
from selenium import webdriver

# Enter path to your browsers driver
driver_path = r"path/to/browserdriver"
# Replace Chrome() with your browser
driver = webdriver.Chrome(driver_path)

def signIn():  
    url = "https://github.com/login"
    driver.get(url)

    username = driver.find_element_by_id("login_field")
    password = driver.find_element_by_id("password")

    # Enter your GitHub username and password
    username.send_keys("username")
    password.send_keys("password")

    driver.find_element_by_name("commit").click()

def createRepo(name):
    driver.get("https://github.com/new")
    repo = driver.find_element_by_id("repository_name")
    repo.send_keys(name)

    driver.find_element_by_css_selector("button.first-in-line").submit()

if __name__ == "__main__":
    name = sys.argv[1]
    signIn()
    createRepo(name)
