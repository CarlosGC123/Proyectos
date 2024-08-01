from .BasePage import BasePage
from selenium.webdriver.common.by import By

#Clase que contiene los métodos interactivos de Login


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def iniciar_sesion(self, username, password):
        self.enviar_texto(By.NAME, "username", username)
        self.enviar_texto(By.NAME, "password", password)
        self.hacer_click(By.XPATH, "//input[@value='Log In']")

    def valida_login(self):
        mensaje = "Accounts Overview"
        return self.valida_texto_elemento(By.CSS_SELECTOR, "h1", mensaje)

