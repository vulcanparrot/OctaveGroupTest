class LandingPage():
    def __inti__(self, driver):
        self.driver = driver
        
        self.loginbutton_css = "#main > div > div.Root__top-container > div.Root__top-bar > header > div:nth-child(5) > button._3f37264be67c8f40fa9f76449afdb4bd-scss._1f2f8feb807c94d2a0a7737b433e19a8-scss"

    def click_loginbutton(self):
        self.find_element_by_css_selector(self.loginbutton_css).click()
