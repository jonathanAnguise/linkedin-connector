from selenium import webdriver
from selenium.webdriver.common.by import By


class WindowHandler():
    def __init__(self, file_path='./'):
        self.path = file_path
        self.driver = webdriver.Chrome()

        self.driver.get('https://linkedin.com')

    def connect_to_linkedin(self, email, password):
        # Select email input
        (email_div, password_div) = self.driver.find_element(By.CLASS_NAME, "sign-in-form__form-input-container") \
            .find_elements(By.TAG_NAME, 'div')
        email_div.find_element(By.TAG_NAME, 'input').send_keys(email)
        password_div.find_element(By.TAG_NAME, 'input').send_keys(password)
        sign_in_button = self.driver.find_element(By.CLASS_NAME, "sign-in-form__submit-button")
        sign_in_button.click()

    def open_new_tab_with_url(self, url):
        self.driver.switch_to.new_window('tab')
        self.driver.get(url)


if __name__ == '__main__':
    print("Should not be executed alone")
