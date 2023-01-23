import time

from selenium import webdriver
from connect_manager import *
from dotenv import dotenv_values
from file_manager import *

if __name__ == '__main__':
    env_var = dotenv_values()
    linkedin_session = WindowHandler()
    answer = None
    while answer != 'y' or answer != 'n':
        print("Do you want to connect manually or using default account? y/n")
        answer = input()
        if answer == 'y':
            linkedin_session.connect_to_linkedin(env_var.get("EMAIL"),
                                                 env_var.get("PASSWORD_LINKEDIN"))
        elif answer == 'n':
            print("Enter your credentials and after type enter")
            input()
            linkedin_session.connect_to_linkedin()
    my_file_manager = FileManager()
    my_file_manager.load_url()
    for url in my_file_manager.url_list:
        # Open and navigate new tab
        linkedin_session.open_new_tab_with_url(url)
        connect_list_button = linkedin_session.driver.find_elements(By.CSS_SELECTOR, '.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
        connect_list_button[1].click()
        time.sleep(5)
        linkedin_session.driver.find_element(By.CSS_SELECTOR, '[aria-label="Add a note"]')
        time.sleep(1)
        linkedin_session.driver.find_element(By.CSS_SELECTOR, 'textarea').send_keys("Hello my name is John, could we connect?")
        

        # TODO 2: Connect with the potential candidate
    input()
