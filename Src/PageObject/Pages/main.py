import time


class MainPage():
    def __init__(self, driver):
        self.driver = driver

        self.banner_css = "#onetrust-close-btn-container > button"
        self.play_button_css = "#main > div > div.Root__top-container > div.Root__now-playing-bar > footer > div > div._985ee24884f107a290cef7577b8a8909-scss > div > div.player-controls__buttons > button._82ba3fb528bb730b297a91f46acd37a3-scss"
        self.next_button_css = "#main > div > div.Root__top-container > div.Root__now-playing-bar > footer > div > div._985ee24884f107a290cef7577b8a8909-scss > div > div.player-controls__buttons > button.bf01b0d913b6bfffea0d4ffd7393c4af-scss"
        self.previous_button_css = "#main > div > div.Root__top-container > div.Root__now-playing-bar > footer > div > div._985ee24884f107a290cef7577b8a8909-scss > div > div.player-controls__buttons > button.bc13c597ccee51a09ec60253c3c51c75-scss"

    def close_banner(self):
        self.driver.find_element_by_css_selector(self.banner_css).click()
        print("banner closed")

    def click_play_button(self):
        self.driver.find_element_by_css_selector(self.play_button_css).click()
        print("playing music")
        time.sleep(5)

    def current_song(self):
        songtitle = self.driver.title
        print(songtitle)

    def next_song(self):
        self.driver.find_element_by_css_selector(self.next_button_css).click()
        print("playing next song")
        time.sleep(5)

    def previous_song(self):
        self.driver.find_element_by_css_selector(self.play_button_css).click()
        self.driver.find_element_by_css_selector(self.previous_button_css).click()
        self.driver.find_element_by_css_selector(self.previous_button_css).click()
        print("playing previous song")
        time.sleep(5)




