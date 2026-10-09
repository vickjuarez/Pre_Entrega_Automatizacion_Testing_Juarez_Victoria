from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 # desde selenium importame a este archivo y que espere , que no se cierre si tarda mas de un micro segundo en cargar la pagina y que espere a que se cargue el elemento que le estoy pidiendo, 
 # y que si no se carga en el tiempo que le estoy pidiendo me tire un error

class LoginPage:
     def __init__(self, driver):
         #definiendo el constructor , para recibir el driver de selenium y poder interactuar con la página de login
         self.driver = driver
         self.username_input = (By.ID, "user-name")
         self.password_input = (By.ID, "password")
         self.login_button = (By.ID, "login-button")
#entrando a la pagina de login y definiendo los localizadores de los elementos que voy a utilizar en la pagina de login, que son el input de usuario, el input de contraseña y el boton de login

     def enter_username(self, username):
          element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_input))
          element.send_keys(username)

     def enter_password(self, password):
         element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input))
         element.send_keys(password)

     def click_login(self):
         element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button))
         element.click()

  
    