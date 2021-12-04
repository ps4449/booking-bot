# File for methods to parse the specific data
# from each available hotel/deal
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BookingReport:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.get_deal_hotels()

    def get_deal_hotels(self):
        return self.boxes_section_element.find_elements(By.CLASS_NAME, '_5d6c618c8')

    def get_deal_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element(By.CLASS_NAME, '_c445487e2').get_attribute('innerHTML').strip() # Hotel name
            hotel_price_html = deal_box.find_element(By.CLASS_NAME, '_e885fdc12').get_attribute('innerHTML')
            hotel_price = hotel_price_html.replace("&nbsp", "")
            hotel_score = deal_box.find_element(By.CLASS_NAME, 'bd528f9ea6').get_attribute('innerHTML')

            collection.append([hotel_name, hotel_price, hotel_score])
        return collection
