import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from pages.pages import HomePage, ItemPage, SearchResultsPage
from pages import locators

# данные товара по которым ищем
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


class Test(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.ozon.ru/")
        
    def tearDown(self):
        self.driver.quit()
        
    def test_searching_by_title_and_adding_to_cart(self):
        page = HomePage(self.driver)
        result = page.find(TITLE)
        WebDriverWait(self.driver, 10).until(EC.url_changes)
        # Если попадаем на страницу товара --- возвращает ItemPage()
        if "http://www.ozon.ru/context/detail/id/" in self.driver.current_url:
            item_page = ItemPage(self.driver)
        # Если попали на страницу с несколькими результатами, сортируем по увеличению цены и выбираем самый дешевый
        else:
            result = SearchResultsPage(self.driver)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locators.SearchResultsLocators.SORTING_DROPDOWN_MENU))
            result.sort("price")
            item_page = result.click_item(1)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "bItemName")))
        # проверяем, что попали на нужную страницу товара
        self.assertEqual(self.driver.current_url, URL)
        # добавляем товар в корзину
        time.sleep(5)
        item_page.add_to_cart()
        # добавлем еще один экземпляр
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locators.ItemPageLocators.PLUS_ONE_BUTTON))
        item_page.add_one_more()
        # переходим в корзину, проверяем, что там 2 экземпляра товара
        cart_page = item_page.go_to_cart()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators.CartPageLocators.TOTAL_QUANTITY))
        self.assertEqual(cart_page.get_total_quanity(), 2)
        # уменьшаем кол-во товара на 1, проверяем, что уменьшилось
        cart_page.minus_one()
        # костыль
        time.sleep(5)
        self.assertEqual(cart_page.get_total_quanity(), 1)
        # удаляем заказ, возвращаемся на главную страницу
        cart_page.remove_all()
        homepage = cart_page.go_home()
        WebDriverWait(self.driver, 10).until(EC.url_changes)
        self.assertEqual(self.driver.current_url, "http://www.ozon.ru/")
              
    def test_registration(self):
        page = HomePage(self.driver)
        registration_page = page.register()
        logged_in_page = registration_page.register(FIRST_NAME, LAST_NAME, EMAIL, PASSWORD)
        # проверяет, что мы залогинились. Должно отображаться имя вместо "Мой OZON".
        self.assertNotEqual(page.get_user(), "Мой OZON")
        logged_in_page.log_off()
        # проверяет, что разлогинились. Должно отображаться "Мой OZON" вместо имени.
        self.assertEqual(page.get_user(), "Мой OZON")
    
    
    def test_logging_in_and_off(self):
        page = HomePage(self.driver)
        logged_in_page = page.log_in(LOGIN_EXISTING, PASSWORD_EXISTING)
        # костыль
        time.sleep(5)
        # проверяет, что мы залогинились. Должно отображаться имя вместо "Мой OZON". 
        self.assertNotEqual(logged_in_page.get_user(), "Мой OZON")
        homepage = logged_in_page.log_off()
        # проверяет, что разлогинились. Должно отображаться "Мой OZON" вместо имени.
        self.assertEqual(homepage.get_user(), "Мой OZON")
    
    
if __name__ == "__main__":
    unittest.main()