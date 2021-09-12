import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.get("https://www.vatanbilgisayar.com/")
    driver.maximize_window()
    driver.implicitly_wait(8)
    request.cls.driver = driver
    yield
    driver.close()