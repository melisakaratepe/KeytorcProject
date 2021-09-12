from selenium.webdriver.common.by import By


class Favoritepage():
    def __init__(self, driver):
        self.driver = driver

    productname = (By.CSS_SELECTOR, "div[class='basket-cart__product-name']")
    removefavorite= (By.XPATH, "//div[@class='basket-cart__table-row']/div[4]/a")
    text= (By.XPATH,"//p[contains(text(),'Favori ürünlerinizi takip edebilirsiniz.')]")

    def getproductname(self):
        return self.driver.find_element(*Favoritepage.productname)

    def removefavorite(self):
        return self.driver.find_element(*Favoritepage.removefavorite)

    def gettext(self):
        return self.driver.find_element(*Favoritepage.gettext)


