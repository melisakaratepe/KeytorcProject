from selenium.webdriver.common.by import By


class Productspage():
    def __init__(self, driver):
        self.driver = driver

    message= (By.XPATH, "//span[contains(text(),'563 adet ürün bulundu.')]")
    pagination= (By.XPATH, "//ul[@class='pagination']/li[2]/a")
    addproduct= (By.XPATH,"//div[@class='wrapper-product wrapper-product--list-page clearfix']/div[3]/div[1]")
    favicon= (By.ID,"fav_Icon")
    closepopup= (By.XPATH,"//body/div[@id='fancybox-container-1']/div[2]/div[4]/div[1]/div[1]/button[1]/*[1]")
    myaccount= (By.ID,"btnMyAccount")
    favoriteproducts= (By.XPATH,"//a[contains(text(),'Favori Ürünlerim')]")

    def getmessage(self):
        return self.driver.find_element(*Productspage.message)

    def getpagination(self):
        return self.driver.find_element(*Productspage.pagination)

    def addproduct(self):
        return self.driver.find_element(*Productspage.addproduct)

    def getfavicon(self):
        return self.driver.find_element(*Productspage.favicon)

    def closepopup(self):
        return self.driver.find_element(*Productspage.closepopup)

    def getmyaccount(self):
        return self.driver.find_element(*Productspage.myaccount)

    def getfavoriteproducts(self):
        return self.driver.find_element(*Productspage.favoriteproducts)



