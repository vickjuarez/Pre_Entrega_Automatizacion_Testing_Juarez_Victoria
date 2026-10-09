import pytest
from login_page import LoginPage
from inventory_page import Inventory_Page

def test_add_product_to_cart(setup_driver):
    # 1. Login exitoso
    login_page = LoginPage(setup_driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory_page = Inventory_Page(setup_driver)

    # 2. Obtener el nombre del primer producto antes de agregarlo para comparar después
    product_name = inventory_page.get_first_product_name()

    # 3. Añadir el primer producto al carrito
    inventory_page.click_add_to_cart_first()

    # 4. Verificar que el contador del carrito se incremente a "1"
    badge_text = inventory_page.get_cart_badge_text()
    assert badge_text == "1", f"El contador del carrito debería ser 1, pero es {badge_text}"

    # 5. Navegar al carrito de compras
    inventory_page.click_cart()

    print("¡Producto añadido al carrito y navegación completada con éxito!")

    #cree este archivo para la organizacion de pruebas, para enumerarlas como si fueran items 