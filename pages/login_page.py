class LoginPage:
    def __init__(self,page):
        self.page=page

    def open_login_page(self):
        self.page.goto("https://ppswportal.csmpl.com/")

    def enter_username(self,username):
        #self.page.get_by_role("textbox", name="Username").nth(0).fill(username)
        self.page.locator("input[placeholder='User Name']").fill(username)

    def wait_for_captcha(self):
        input("manually complete the recaptcha and press enter")

    def next_button(self):
        self.page.locator("button[type='submit']").click()

    def login_with_password(self):
        self.page.locator("//a[text()='Login with Password']").click()
        #input("wait for next action")
    
    def enter_password(self,password):
        self.page.locator("//input[@name='password']").fill(password)

    def click_login_button(self):
        self.page.get_by_role("button", name="Login").click()
       
        
        
        