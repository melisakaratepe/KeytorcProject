import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from BaseClass import BaseClass
from page_objects.Favoritepage import Favoritepage
from page_objects.Homepage import Homepage
from page_objects.Loginpage import Loginpage
from page_objects.Productspage import Productspage


class TestOne(BaseClass):
    def test_e2e(self, setup):
        try:
            element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//html')))
            print("Home Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        self.driver.find_element_by_xpath("//span[@id='type']").click()
        self.driver.find_element_by_xpath("//a[contains(text(), 'Giriş Yap')]").click()
        loginpage = Loginpage(self.driver)
        loginpage.getemail().send_keys("test1234@gmail.com")
        loginpage.getpassword().send_keys("Test1234")
        loginpage.getloginbutton().click()
        homepage = Homepage(self.driver)
        self.driver.find_element_by_xpath("//input[@id='navbar-search-input']").send_keys("samsung")
        homepage.getsearchicon().click()
        time.sleep(5)
        productspage = Productspage(self.driver)
        message = productspage.getmessage().text
        assert message == "563 adet ürün bulundu."
        productspage.getpagination().click()
        self.driver.find_element_by_xpath(
            "//div[@class='wrapper-product wrapper-product--list-page clearfix']/div[3]/div[1]").click()
        productspage.getfavicon().click()
        self.driver.find_element_by_xpath(
            "//body/div[@id='fancybox-container-1']/div[2]/div[4]/div[1]/div[1]/button[1]/*[1]").click()
        productspage.getmyaccount().click()
        productspage.getfavoriteproducts().click()
        favoritepage= Favoritepage(self.driver)
        text = favoritepage.getproductname().text
        assert "SM-G998BZKGTUR" in text
        self.driver.find_element_by_xpath("//div[@class='basket-cart__table-row']/div[4]/a").click()
        fav = self.driver.find_element_by_xpath("//p[contains(text(),'Favori ürünlerinizi takip edebilirsiniz.')]").text
        assert fav == "Favori ürünlerinizi takip edebilirsiniz."
