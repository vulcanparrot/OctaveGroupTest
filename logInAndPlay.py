import getpass
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


from Src.PageObject.Pages.landing import LandingPage
from Src.PageObject.Pages.login import LoginPage
from Src.PageObject.Pages.main import MainPage

class LoginAndPlay(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("FILLIN")
        url = "https://open.spotify.com/"
        cls.driver.get(url)
        cls.username = "FILLIN"
        cls.password = "FILLIN"
        cls.wait = WebDriverWait(cls.driver, 8)


    # fail if not logged in
    # fail if logged in elsewhere and playing

    def test_login_valid(self):
        driver = self.driver
        driver.implicitly_wait(30)

        landing = LandingPage(driver)
        landing.click_loginbutton()

        login = LoginPage(driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()

        main=MainPage(driver)
        time.sleep(3)
        main.close_banner()
        main.current_song()
        title0 = driver
        main.click_play_button()
        main.current_song()
        title1 = driver.title
        title1 != title0
        print("song playing confirmed")
        main.next_song()
        main.current_song()
        title2 = driver.title
        title1 != title2
        print("song change confirmed")
        main.previous_song()
        main.current_song()
        title3 = driver.title
        title2 !=title3
        print("song change confirmed")
        title1 == title3
        print("original song confirmed")
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")


if __name__ == '__main__':
    unittest.main()