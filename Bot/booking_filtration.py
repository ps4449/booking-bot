from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # def apply_star_rating(self, *star_values):
    #     star_rating_box = self.driver.find_element(By.ID, 'filter_class')
    #     star_element = star_rating_box.find_elements_by_css_selector('*')
    #
    #     print(len(star_element))
    #
    #     for star_value in star_values:
    #         for star in star_element:
    #             if str(star.get_attribute('innerHTML')).strip() == f'{star_value} stars':
    #                 star.click()
    #
    # def sort_price_lowest_first(self):
    #     element = self.driver.find_element(By.CSS_SELECTOR, 'li[data-id="price"]')
    #     element.click()
