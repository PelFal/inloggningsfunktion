import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

from selenium.webdriver.common.by import By

class TestLogin():

    def test_positive_login(self, driver):
        # Go to webpage
        driver.get("https://www.saucedemo.com")
        time.sleep(2)

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "user-name")
        username_locator.send_keys("standard_user")

        # Type password secret_sauce into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("secret_sauce")

        driver.find_element(By.ID, "login-button").click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("inventory.html")
        )

        # Verify new page has url https://www.saucedemo.com/inventory.html
        assert "inventory.html" in driver.current_url
        inventory = driver.find_element(By.CLASS_NAME, "inventory_list")
        assert inventory.is_displayed()
     # test av commit
