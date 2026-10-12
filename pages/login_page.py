from pages.Base_Page import BasePage
from config.config import BASE_URL
class LoginPage(BasePage):
    '''def __init__(self,page):
        super().__init__(page) '''       

    def open_login_page(self):
        #self.page.goto("https://ppswportal.csmpl.com/")
        self.page.goto(BASE_URL)

    def enter_username(self,username):
        #self.page.get_by_role("textbox", name="Username").nth(0).fill(username)
        #self.page.locator("input[placeholder='User Name']").fill(username)
        #self.fill("input[placeholder='User Name']",username) this is from base page 
        self.fill(self.page.locator("input[placeholder='User Name']"),username)
        

    def wait_for_captcha(self):
        input("manually complete the recaptcha and press enter")

    def next_button(self):
        #self.page.locator("button[type='submit']").click()
        self.click(self.page.locator("button[type='submit']"))

    def login_with_password(self):
        #self.page.locator("//a[text()='Login with Password']").click()
        #input("wait for next action")
        self.click(self.page.locator("//a[text()='Login with Password']"))
    
    def enter_password(self,password):
        #self.page.locator("//input[@name='password']").fill(password) 
        #self.fill("input[placeholder='Password']", password)   this is from base page
        self.fill(self.page.locator("//input[@name='password']"),password)

    def click_login_button(self):
        self.page.get_by_role("button", name="Login").click()
       
        
        
        