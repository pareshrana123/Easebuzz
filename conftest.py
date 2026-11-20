
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Launch Chrome browser
    driver = webdriver.Chrome()

    # Maximize browser
    driver.maximize_window()

    # Open practice website
    driver.get(
        "https://rahulshettyacademy.com/AutomationPractice/"
    )

    yield driver

    # Close browser after test
    driver.quit()
