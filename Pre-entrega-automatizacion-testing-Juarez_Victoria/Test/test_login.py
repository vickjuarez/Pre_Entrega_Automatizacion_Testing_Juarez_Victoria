import pytest

from selenium import webdriver #importando la biblioteca de selenium para poder interactuar con el navegador

from login_page import LoginPage#importando los componentes de la página de login 

def test_usuario_exitoso(setup_driver):# le explico al test cuales son los datos "correctos" para poder loguearse y que el test sea exitoso
 username = "standard_user" 
 password = "secret_sauce"
 # guardo en la memoria de la compu los parametros correctos 
 login_page = LoginPage(setup_driver) #le digo al codigo que lo que esta en mi pagina de componentes es lo mismo de la url que estoy probando
 
 login_page.enter_username(username) 
 login_page.enter_password(password)
 login_page.click_login()

 assert "inventory.html" in setup_driver.current_url
