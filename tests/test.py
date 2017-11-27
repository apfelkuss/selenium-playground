import unittest
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import CartPageLocators as cartloc
from pages.locators import SearchResultsPageLocators as searchloc
from pages.locators import UserPageLocators as userloc
from pages.pages import GuestPage, SearchResultsPage


###############################################################################
# Тестовые данные
# данные для поиска
ISBN = "978-0-7515-6536-2"
TITLE = "Harry Potter and the cursed child"
URL = "http://www.ozon.ru/context/detail/id/140983994/"
# данные существующего аккаунта
LOGIN_EXISTING = "s491513@mvrht.net"
PASSWORD_EXISTING = "qwerty"
# данные для регистрации
FIRST_NAME = "Иван"
LAST_NAME = "Иванов"
EMAIL = "s491513+test{}@mvrht.net".format(time.time())
PASSWORD = "qwerty"

###############################################################################


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('http://www.ozon.ru/')
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_searching_by_name(self):
        page = GuestPage(self.driver)
        result = page.find(TITLE) # можно искать по ISBN
        """Если поиск возвращает страницу с несколькими товарами, 
        сортируем по увеличению цены и выбираем самый дешевый.
        """
        if isinstance(result, SearchResultsPage):
            self.wait.until(EC.presence_of_element_located(
                            searchloc.SORTING_DROPDOWN_MENU))
            result.sort("price")
            item_page = result.click_item(1)
            self.wait.until(EC.presence_of_element_located(
                            (By.CLASS_NAME, "bItemName")))
        else:
            item_page = result
        # Проверяем, что попали на страницу нужного товара.
        self.assertEqual(self.driver.current_url, URL)

        """Почему-то item_page.add_to_cart() срабатывает не всегда,
        из-за чего вылетает NoSuchElementExceptio при вызове
        item_page.add_to_cart().
        При этом item_page.add_to_cart() ошибку не выдает.
        Попытался решить через while.
        """
        while True:
            try:
                item_page.add_one_more()
            except NoSuchElementException:
                item_page.add_to_cart()
            else:
                break

        # Проверяем, что в корзине 2 экземпляра товара.
        cart_page = item_page.go_to_cart()
        self.wait.until(EC.visibility_of_element_located(
                        cartloc.TOTAL_QUANTITY))
        self.assertEqual(cart_page.get_total_quanity(), 2)
        # Уменьшаем кол-во товара на 1, проверяем, что кол-во уменьшилось.
        cart_page.minus_one()
        self.wait.until(lambda driver: driver.execute_script(
                        "return jQuery.active == 0"))
        self.assertEqual(cart_page.get_total_quanity(), 1)
        # Удаляем заказ, возвращаемся на главную страницу.
        cart_page.remove_all()
        homepage = cart_page.go_home()
        self.wait.until(EC.url_changes)
        self.assertEqual(self.driver.current_url, "http://www.ozon.ru/")

    def test_registration(self):
        page = GuestPage(self.driver)
        registration_page = page.register()
        logged_in_page = registration_page.register(FIRST_NAME, 
                                                    LAST_NAME, 
                                                    EMAIL, 
                                                    PASSWORD)
        # Проверяем, что залогинились.
        self.assertEqual(page.get_user(), FIRST_NAME)
        logged_in_page.log_off()
        # Проверяем, что разлогинились.
        self.assertEqual(page.get_user(), "Мой OZON")


    def test_logging_in_and_off(self):
        page = GuestPage(self.driver)
        logged_in_page = page.log_in(LOGIN_EXISTING, PASSWORD_EXISTING)
        # Проверяем, что залогинились.
        self.wait.until(EC.presence_of_element_located(
                        (userloc.LOG_OFF_BUTTON)))
        self.assertEqual(logged_in_page.get_user(), FIRST_NAME)
        homepage = logged_in_page.log_off()
        # Проверяем, что разлогинились.
        self.assertEqual(homepage.get_user(), "Мой OZON")


if __name__ == "__main__":
    unittest.main()
