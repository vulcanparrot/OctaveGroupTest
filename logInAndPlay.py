import getpass
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from Src.PageObject.Pages.landing import LandingPage
from Src.PageObject.Pages.login import LoginPage

class LoginAndPlay(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("D:\Repos\octavetest\chromedriver.exe")
        url = "https://open.spotify.com/"
        cls.driver.get(url)
        username = input("What's your spotify username or email? ")
        password = getpass.getpass("What's your spotify password? ")


# fail if not logged in
# get tags and make objects for the following

    def test_login_valid(self):
        driver = self.driver
        driver.get(url)

        landing = LandingPage(driver)
        landing.click_loginbutton()

        login = LoginPage(driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")


if __name__ == '__main__':
    unittest.main()