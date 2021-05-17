class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.username_field_css = "#login-username"
        self.password_field_css = "#login-password"
        self.login_button_css = "#login-button"
        
    def enter_username(self, username):
        self.driver.find_element_by_css_selector(self.username_field_css).clear()
        self.driver.find_element_by_css_selector(self.username_field_css).send_keys(username)
        print("username entered")

    def enter_password(self, password):
        self.driver.find_element_by_css_selector(self.password_field_css).clear()
        self.driver.find_element_by_css_selector(self.password_field_css).send_keys(password)
        print("password entered")

    def click_login(self):
        self.driver.find_element_by_css_selector(self.login_button_css).click()
        print("log in button clicked")


# fail banner is ("body > div.ng-scope > div.container-fluid.login.ng-scope > div > div:nth-child(2) > div > p > span")