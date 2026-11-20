import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://rahulshettyacademy.com/AutomationPractice/"


# --------------------------------
# Test 1: Verify Page Title
# --------------------------------

def test_page_title_validation(driver):

    assert "Practice" in driver.title


# --------------------------------
# Test 2: Select Radio Button
# --------------------------------

def test_radio_button_validation(driver):

    radio2 = driver.find_element(
        By.XPATH, "//input[@value='radio2']"
    )

    radio2.click()

    assert radio2.is_selected()


# --------------------------------
# Test 3: Select Checkboxes
# --------------------------------

def test_checkboxes_validation(driver):

    option1 = driver.find_element(
        By.XPATH, "//input[@value='option1']"
    )

    option3 = driver.find_element(
        By.XPATH, "//input[@value='option3']"
    )

    option1.click()
    option3.click()

    assert option1.is_selected()
    assert option3.is_selected()


# --------------------------------
# Test 4: Select Dropdown Option
# --------------------------------

def test_dropdown_validation(driver):

    dropdown = Select(
        driver.find_element(
            By.ID, "dropdown-class-example"
        )
    )

    dropdown.select_by_visible_text("Option2")

    selected_option = dropdown.first_selected_option.text

    assert selected_option == "Option2"


# --------------------------------
# Test 5: Enter Text in Textbox
# --------------------------------

def test_enter_name_validation(driver):

    name_input = driver.find_element(
        By.ID, "name"
    )

    name_input.send_keys("Automation Tester")

    assert name_input.get_attribute("value") == "Automation Tester"


# --------------------------------
# Test 6: Handle JavaScript Alert
# --------------------------------

def test_javascript_alert_validation(driver):

    name_input = driver.find_element(
        By.ID, "name"
    )

    name_input.send_keys("Automation Tester")

    alert_button = driver.find_element(
        By.ID, "alertbtn"
    )

    alert_button.click()

    # Wait for alert
    wait = WebDriverWait(driver, 10)

    alert = wait.until(
        EC.alert_is_present()
    )

    alert_text = alert.text

    assert "Automation Tester" in alert_text

    # Accept alert
    alert.accept()
