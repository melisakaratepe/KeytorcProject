from selenium.webdriver.common.by import By


class Homepage():
    def __init__(self, driver):
        self.driver = driver

    searchinput = (By.XPATH, "//input[@id='navbar-search-input']")
    searchicon = (By.CSS_SELECTOR, "span[class='icon-search']")


    def getsearchinput(self):
        return self.driver.find_element(*Homepage.searchinput)

    def getsearchicon(self):
        return self.driver.find_element(*Homepage.searchicon)
