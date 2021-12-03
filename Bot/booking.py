import os
import Bot.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from Bot.booking_filtration import BookingFiltration


class Booking(webdriver.Chrome):
    def __init__(self, driver_path = r"C:\SeleniumDrivers", teardown = False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options = options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def first_page(self):
        self.get(const.URL)

    def change_currency(self, currency=None):
        curr_btn = self.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]')
        curr_btn.click()

        selected_curr = self.find_elements(By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_curr[0].click()

    def select_place(self, place):
        search_field = self.find_element(By.ID, 'ss')
        search_field.clear()
        search_field.send_keys(place)

        first_result = self.find_elements(By.CSS_SELECTOR, 'li[data-i="0"]')
        first_result[0].click()

    def select_dates(self, checkin, checkout):
        checkin = self.find_elements(By.CSS_SELECTOR, f'td[data-date="{checkin}"]')
        checkin[0].click()

        checkout = self.find_elements(By.CSS_SELECTOR, f'td[data-date="{checkout}"]')
        checkout[0].click()

    def select_members(self, count):
        selection_element = self.find_element(By.ID, 'xp__guests__toggle')
        selection_element.click()

        while True:
            decrease_adults = self.find_elements(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
            decrease_adults[0].click()

            adults_value_ele = self.find_element(By.ID, 'group_adults')
            adults_value = adults_value_ele.get_attribute('value')

            if int(adults_value) == 1:
                break

        increase_adults = self.find_elements(By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')
        for i in range(1, count):
            increase_adults[0].click()

    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_button.click()

    def apply_filtration(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(3, 4, 5)
        filtration.sort_price_lowest_first()
