from .BasePage import BasePage
from selenium.webdriver.common.by import By

#Clase que contiene los métodos interactivos de la página principal


class InicioPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def presionar_registro(self):
        self.hacer_click(By.LINK_TEXT, "Register")

    def cerrar_sesion(self):
        self.hacer_click(By.LINK_TEXT, "Log Out")

