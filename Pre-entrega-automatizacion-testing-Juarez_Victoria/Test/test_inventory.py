import pytest
from login_page import LoginPage
from inventory_page import Inventory_Page

def test_inventory_page_title(setup_driver):
        # 1. Nos logueamos
    login_page = LoginPage(setup_driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    
    # 2. Validamos el título 
    inventory_page = Inventory_Page(setup_driver)
    title_text = inventory_page.get_title_text()
    assert title_text == "Products"
    # 3. Validamos la presencia de productos 
    products = setup_driver.find_elements(*inventory_page.PRODUCTS)
    assert len(products) > 0, "No se encontraron productos en la página de inventario"

    # 4. Validamos y obtenemos el nombre y el precio del primer producto usando los métodos nuevos
    first_name = inventory_page.get_first_product_name()
    first_price = inventory_page.get_first_product_price()
    
    print(f"Primer producto encontrado: {first_name} - Precio: {first_price}")
    
    assert first_name != "", "El nombre del primer producto está vacío"
    assert first_price != "", "El precio del primer producto está vacío"
    

    