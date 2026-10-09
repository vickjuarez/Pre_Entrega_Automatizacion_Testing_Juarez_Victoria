import pytest #es la biblioteca propia de phyton que me permite hacer pruebas de manera 

from selenium import webdriver

@pytest.fixture #para no tener que repetir el código de configuración del driver en cada prueba,  cree un fixture que se ejecuta antes de cada prueba y se encarga de configurar el driver y devolverlo a la prueba
def setup_driver(): #definiendo el set up del driver, que es la configuración del navegador que se va a utilizar para la preparacion de una prueba 
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()