from BasePage import BasePage
from selenium.webdriver.common.by import By


class InicioPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def ir_a_registro(self):
        self.hacer_click(By.LINK_TEXT, "Register")

    def cerrar_sesion(self):
        self.hacer_click(By.LINK_TEXT, "Log Out")

