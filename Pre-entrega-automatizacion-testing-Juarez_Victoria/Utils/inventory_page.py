from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Inventory_Page:
# Guardo todos los localizadores de la página de productos (título, primer producto, precio, y los elementos nuevos para manejar el carrito de compras).
    
    TITLE_TEXT = (By.CLASS_NAME, "title")
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    FIRST_PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    FIRST_PRODUCT_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")
    ADD_TO_CART_FIRST = (By.CSS_SELECTOR, ".inventory_item:first-child button")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    # Recibo el driver de Selenium para poder interactuar con los elementos de esta pantalla.
    def __init__(self, driver):
        self.driver = driver
    # Espero a que cargue el elemento en pantalla y devuelvo el texto (por ejemplo, el título o el nombre del producto).
    def get_title_text(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TITLE_TEXT)
        ).text

    def get_first_product_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.FIRST_PRODUCT_NAME)
        ).text

    def get_first_product_price(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.FIRST_PRODUCT_PRICE)
        ).text
    # Acciones del usuario: hago clic para agregar el primer producto al carrito, 
    # leo el numerito que marca el carrito, o hago clic para entrar a verlo.
    def click_add_to_cart_first(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*self.ADD_TO_CART_FIRST)
        ).click()

    def get_cart_badge_text(self):
        return WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*self.CART_BADGE)
        ).text

    def click_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
