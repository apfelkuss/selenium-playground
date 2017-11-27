import time

from selenium.webdriver.common.keys import Keys

from pages.locators import BasePageLocators as baseloc
from pages.locators import GuestPageLocators as guestloc
from pages.locators import UserPageLocators as userloc
from pages.locators import RegistrationPageLocators as regloc
from pages.locators import SearchResultsPageLocators as searchloc
from pages.locators import ItemPageLocators as itemloc
from pages.locators import CartPageLocators as cartloc


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logged_in = False

    def find(self, query):
        search_bar = self.driver.find_element(*baseloc.SEARCH_BAR)
        search_bar.clear()
        search_bar.send_keys(query)
        search_bar.send_keys(Keys.RETURN)
        # костыль
        time.sleep(5)
        if "http://www.ozon.ru/context/detail/id/" in self.driver.current_url:
            print("inside if-loop:", self.driver.current_url)
            return ItemPage(self.driver)
        else:
            print("inside else:", self.driver.current_url)
            return SearchResultsPage(self.driver)

    def get_user(self):
        user = self.driver.find_element(*baseloc.MY_OZON)
        return user.text

    def go_home(self):
        homepage = self.driver.find_element(*baseloc.HOME)
        homepage.click()
        if self.logged_in:
            return UserPage(self.driver)
        else:
            return GuestPage(self.driver)


class GuestPage(BasePage):

    def register(self):
        my_ozon = self.driver.find_element(*baseloc.MY_OZON)
        my_ozon.click()

        log_in_panel = self.driver.find_element(*guestloc.LOG_IN_PANEL)
        log_in_panel.click()

        register_button = self.driver.find_element(*guestloc.REGISTER_BUTTON)
        register_button.click()

        return RegistrationPage(self.driver)

    def log_in(self, login, password):
        my_ozon = self.driver.find_element(*baseloc.MY_OZON)
        my_ozon.click()

        log_in_panel = self.driver.find_element(*guestloc.LOG_IN_PANEL)
        log_in_panel.click()

        login_field = self.driver.find_element(*guestloc.LOGIN_FIELD)
        login_field.send_keys(login)

        password_field = self.driver.find_element(*guestloc.PASSWORD_FIELD)
        password_field.send_keys(password)

        login_button = self.driver.find_element(*guestloc.LOG_IN_BUTTON)
        login_button.click()

        return UserPage(self.driver)


class UserPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.logged_in = True
#        self.driver.implicitly_wait(10)

    def log_off(self):
        my_ozon = self.driver.find_element(*baseloc.MY_OZON)
        my_ozon.click()

        log_off = self.driver.find_element(*userloc.LOG_OFF_BUTTON)
        log_off.click()

        return GuestPage(self.driver)


class SearchResultsPage(BasePage):

    def click_item(self, index):
        # index starts with 1
        results = self.driver.find_elements(*searchloc.ITEMS)
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
            sorting_dropdown_menu = self.driver.find_element(
                    *searchloc.SORTING_DROPDOWN_MENU)
            sorting_dropdown_menu.click()
            if order == "popular":
                self.driver.find_element(*searchloc.SORT_BY_POPULARITY).click()
            elif order == "new":
                self.driver.find_element(*searchloc.SORT_BY_NEWNESS).click()
            elif order == "rating":
                self.driver.find_element(*searchloc.SORT_BY_RATING).click()
            elif order == "price":
                self.driver.find_element(*searchloc.SORT_BY_PRICE).click()
            elif order == "price_desc":
                self.driver.find_element(*searchloc.SORT_BY_PRICE_DESC).click()


class ItemPage(BasePage):

    def add_to_cart(self):
        add_to_cart_button = self.driver.find_element(
                *itemloc.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def add_one_more(self):
        plus_one = self.driver.find_element(*itemloc.PLUS_ONE_BUTTON)
        plus_one.click()

    def go_to_cart(self):
        go_to_cart = self.driver.find_element(*itemloc.GO_TO_CART_BUTTON)
        go_to_cart.click()
        return CartPage(self.driver)


class CartPage(BasePage):

    def remove_all(self):
        remove_all = self.driver.find_element(*cartloc.REMOVE_ALL)
        remove_all.click()

    def restore_all(self):
        restore_all = self.driver.find_element(*cartloc.RESTORE_ALL)
        restore_all.click()

    def plus_one(self):
        plus_one = self.driver.find_element(*cartloc.PLUS_ONE)
        plus_one.click()

    def minus_one(self):
        minus_one = self.driver.find_element(*cartloc.MINUS_ONE)
        minus_one.click()

    def get_total_quanity(self):
        total_quantity_text = self.driver.find_element(*cartloc.TOTAL_QUANTITY)
        total_quantity = int(total_quantity_text.text.split()[0])
        return total_quantity


class RegistrationPage(BasePage):

    def register(self, fname, lname, email, password):
        private_individual = self.driver.find_element(*regloc.PRIVATE_INDIVIDUAL)
        if private_individual.get_attribute("checked") != "true":
            private_individual.click()

        fname_field = self.driver.find_element(*regloc.FIRST_NAME)
        fname_field.clear()
        fname_field.send_keys(fname)

        lname_field = self.driver.find_element(*regloc.LAST_NAME)
        lname_field.clear()
        lname_field.send_keys(lname)

        email_field = self.driver.find_element(*regloc.EMAIL)
        email_field.clear()
        email_field.send_keys(email)

        password_field = self.driver.find_element(*regloc.PASSWORD)
        password_field.clear()
        password_field.send_keys(password)

        confirm_password_field = self.driver.find_element(*regloc.CONFIRM_PASSWORD)
        confirm_password_field.clear()
        confirm_password_field.send_keys(password)

        registration_button = self.driver.find_element(*regloc.REGISTRATION_BUTTON)
        registration_button.click()

        return UserPage(self.driver)
