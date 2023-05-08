import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_name():
    driver = webdriver.Chrome(
        service=Service(
            r"C:\Users\Shadow\Desktop\python_basics\14.2_Tets_framework\\"
            + "chromedriver.exe"))
    driver.get("https://github.com/login")

    login_elem = driver.find_element(By.ID, "login_field")
    login_elem.send_keys("pavlenkovyacheslav@mistakeinemail.com")

    pass_elem = driver.find_element(By.ID, "password")
    pass_elem.send_keys("wrong_password")

    sign_in_elem = driver.find_element(By.NAME, "commit")
    sign_in_elem.click()

    assert driver.title == "Sign in to GitHub · GitHub"

    driver.close()
