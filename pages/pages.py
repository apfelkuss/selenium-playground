from selenium.webdriver.common.keys import Keys
from pages import locators


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        
    def find(self, query):
        search_bar = self.driver.find_element(*locators.BasePageLocators.SEARCH_BAR)
        search_bar.clear()
        search_bar.send_keys(query)
        search_bar.send_keys(Keys.RETURN)
        
    def get_user(self):
        my_ozon = self.driver.find_element(*locators.BasePageLocators.MY_OZON)
        return my_ozon.text
    
    def go_home(self):
        home = self.driver.find_element(*locators.BasePageLocators.HOME)
        home.click()
        if self.get_user() == "Мой OZON":
            return HomePage(self.driver)
        elif self.get_user() != "Мой OZON":
            return LoggedInPage(self.driver)
        

class HomePage(BasePage):
        
    def register(self):
        my_ozon = self.driver.find_element(*locators.BasePageLocators.MY_OZON)
        my_ozon.click()
        
        login_panel = self.driver.find_element(*locators.HomePageLocators.LOGIN_PANEL)
        login_panel.click()
        
        register_button = self.driver.find_element(*locators.HomePageLocators.REGISTER_BUTTON)
        register_button.click()
        
        return RegistrationPage(self.driver)
        
    def log_in(self, login, password):
        my_ozon = self.driver.find_element(*locators.BasePageLocators.MY_OZON)
        my_ozon.click()
        
        login_panel = self.driver.find_element(*locators.HomePageLocators.LOGIN_PANEL)
        login_panel.click()
        
        login_field = self.driver.find_element(*locators.HomePageLocators.LOGIN_FIELD)
        login_field.send_keys(login)
        
        password_field = self.driver.find_element(*locators.HomePageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        
        login_button = self.driver.find_element(*locators.HomePageLocators.LOGIN_BUTTON)
        login_button.click()

        return LoggedInPage(self.driver)
    

class LoggedInPage(BasePage):
    
    def log_off(self):
        my_ozon = self.driver.find_element(*locators.BasePageLocators.MY_OZON)
        my_ozon.click()
        
        log_off = self.driver.find_element(*locators.LoggedInPageLocators.LOG_OFF)
        log_off.click()
        
        return HomePage(self.driver)


class SearchResultsPage(BasePage):
    
    def click_item(self, index):
        """ 
        index starts with 1
        
        """
        results = self.driver.find_elements(*locators.SearchResultsLocators.ITEMS)
        results[index - 1].click()
        return ItemPage(self.driver)
    
    def sort(self, order="price"):      
        """
        popular --- сначала популярные
        new --- сначала новинки
        rating --- по рейтингу
        price --- по возрастанию цены
        price_desc --- по убыванию цены
        
        """
        valid = ["popular", "new", "rating", "price", "price_desc"]
        if order not in valid:
            raise ValueError("Sorting order must be one of {}.".format(valid))
        else:
            sorting_dropdown_menu = self.driver.find_element(*locators.SearchResultsLocators.SORTING_DROPDOWN_MENU)
            sorting_dropdown_menu.click()
            if order == "popular":
                self.driver.find_element_by_css_selector("[class*=Select_Item][data-value=bests]").click()
            elif order == "new":
                self.driver.find_element_by_css_selector("[class*=Select_Item][data-value=new]").click()
            elif order == "rating":
                self.driver.find_element_by_css_selector("[class*=Select_Item][data-value=rate]").click()
            elif order == "price":
                self.driver.find_element_by_css_selector("[class*=Select_Item][data-value=price]").click()
            elif order == "price_desc":
                self.driver.find_element_by_css_selector("[class*=Select_Item][data-value=price_rev]").click()
                
    def add_to_cart(self):
        
        return CartPage(self.driver)    


class ItemPage(BasePage):
    
    def add_to_cart(self):
        add_to_cart_button = self.driver.find_element(*locators.ItemPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
    
    def add_one_more(self):
        plus_one = self.driver.find_element(*locators.ItemPageLocators.PLUS_ONE_BUTTON)
        plus_one.click()
        
    def go_to_cart(self):
        go_to_cart = self.driver.find_element(*locators.ItemPageLocators.GO_TO_CART_BUTTON)
        go_to_cart.click()
        return CartPage(self.driver)


class CartPage(BasePage):
    
    def remove_all(self):
        remove_all = self.driver.find_element(*locators.CartPageLocators.REMOVE_ALL)
        remove_all.click()
    
    def restore_all(self):
        restore_all = self.driver.find_element(*locators.CartPageLocators.RESTORE_ALL)
        restore_all.click()

    def plus_one(self):
        plus_one = self.driver.find_element(*locators.CartPageLocators.PLUS_ONE)
        plus_one.click()
    
    def minus_one(self):
        minus_one = self.driver.find_element(*locators.CartPageLocators.MINUS_ONE)
        minus_one.click()
    
    def get_total_quanity(self):
        total_quantity_text = self.driver.find_element(*locators.CartPageLocators.TOTAL_QUANTITY)
        total_quantity = int(total_quantity_text.text.split()[0])
        return total_quantity


class RegistrationPage(BasePage):
    
    def register(self, fname, lname, email, password):
        private_individual = self.driver.find_element(*locators.RegistrationPageLocators.PRIVATE_INDIVIDUAL)
        if private_individual.get_attribute("checked") != "true":
            private_individual.click()
        
        fname_field = self.driver.find_element(*locators.RegistrationPageLocators.FIRST_NAME)
        fname_field.clear()
        fname_field.send_keys(fname)
        
        lname_field = self.driver.find_element(*locators.RegistrationPageLocators.LAST_NAME)
        lname_field.clear()
        lname_field.send_keys(lname)
        
        email_field = self.driver.find_element(*locators.RegistrationPageLocators.EMAIL)
        email_field.clear()
        email_field.send_keys(email)
        
        password_field = self.driver.find_element(*locators.RegistrationPageLocators.PASSWORD)
        password_field.clear()
        password_field.send_keys(password)
        
        confirm_password_field = self.driver.find_element(*locators.RegistrationPageLocators.CONFIRM_PASSWORD)
        confirm_password_field.clear()
        confirm_password_field.send_keys(password)
        
        registration_button = self.driver.find_element(*locators.RegistrationPageLocators.REGISTRATION_BUTTON)
        registration_button.click()
        
        return LoggedInPage(self.driver)
