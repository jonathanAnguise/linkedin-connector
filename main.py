from selenium import webdriver
from connect_manager import *
from dotenv import dotenv_values

if __name__ == '__main__':
    env_var = dotenv_values()
    # driver = webdriver.Chrome()
    # driver.get("http://selenium.dev")
    # driver.quit()
    linkedin_session = WindowHandler()
    linkedin_session.connect_to_linkedin(env_var.get("EMAIL"),
                                         env_var.get("PASSWORD_LINKEDIN"))
    input()
