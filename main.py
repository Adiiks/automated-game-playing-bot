from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

start_game_time = int(time.time())
check_upgrades_time = int(time.time())
play_game = True

while play_game:  # run bot
    cookie.click()
    if int(time.time()) - check_upgrades_time == 5:  # for every 5 seconds buy most expensive upgrade
        check_upgrades_time = int(time.time())
        upgrades = driver.find_elements(By.CSS_SELECTOR, "#store div")
        for upgrade in reversed(upgrades):
            if upgrade.get_attribute("class") == "":
                upgrade.click()
                break
    if int(time.time()) - start_game_time == 300:  # after 5 minutes stop bot
        play_game = False

cookies_per_seconds = driver.find_element(By.ID, "cps")
print(cookies_per_seconds.text)
