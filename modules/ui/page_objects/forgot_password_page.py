from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class ForgotPasswordPage(BasePage):
    URL = 'https://github.com/password_reset'

    def __init__(self) -> None:
        super().__init__()

    def go_to_by_url(self):
        self.driver.get(ForgotPasswordPage.URL)

    def go_to_link(self, link):
        self.driver.get(link)
