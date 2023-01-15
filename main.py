from selenium import webdriver
from connect_manager import *
from dotenv import dotenv_values
from file_manager import *

if __name__ == '__main__':
    env_var = dotenv_values()
    # driver = webdriver.Chrome()
    # driver.get("http://selenium.dev")
    # driver.quit()
    linkedin_session = WindowHandler()
    linkedin_session.connect_to_linkedin(env_var.get("EMAIL"),
                                         env_var.get("PASSWORD_LINKEDIN"))
    my_file_manager = FileManager()
    my_file_manager.load_url()
    for url in my_file_manager.url_list:
        # Open and navigate new tab
        linkedin_session.open_new_tab_with_url(url)
        # TODO 2: Connect with the potential candidate
    input()
