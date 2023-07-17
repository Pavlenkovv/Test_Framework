import time
import pytest
from selenium.webdriver.common.by import By
from modules.ui.page_objects.sign_in_page import SignInPage


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    sign_in_page = SignInPage()
    sign_in_page.go_to()
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    sign_in_page.close()


@pytest.mark.ui
def test_check_wrong_password_link_page_object():
    sign_in_page = SignInPage()
    sign_in_page.go_to()
    sign_in_page.click_forgot_password_link()

    assert sign_in_page.check_title("Forgot your password? · GitHub")

    sign_in_page.close()


@pytest.mark.ui
def test_click_on_the_cat_page_object():
    sign_in_page = SignInPage()
    sign_in_page.go_to()
    sign_in_page.driver.find_element(
        By.CSS_SELECTOR, ".octicon.octicon-mark-github"
    ).click()
    time.sleep(2)
    assert sign_in_page.check_title("GitHub: Let’s build from here · GitHub")

    sign_in_page.close()
