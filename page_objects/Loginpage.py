from selenium.webdriver.common.by import By


class Loginpage():
    def __init__(self,driver):
        self.driver = driver
    email= (By.XPATH,"//input[@id='email']")
    password= (By.CSS_SELECTOR, "input[id='pass']")
    loginbutton= (By.ID,"login-button")


    def getemail(self):
        return self.driver.find_element(*Loginpage.email)
    def getpassword(self):
        return self.driver.find_element(*Loginpage.password)
    def getloginbutton(self):
        return self.driver.find_element(*Loginpage.loginbutton)