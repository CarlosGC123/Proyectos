import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import path_chromedriver, link_parabank
from Pages.InicioPage import InicioPage
from Pages.LoginPage import LoginPage
from Pages.RegistroPage import RegistroPage


class ParabankFlujo:
    def __init__(self):
        driver_chrome = Service(executable_path=path_chromedriver)
        self.driver = webdriver.Chrome(service=driver_chrome)
        self.inicio_page = InicioPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.registro_page = RegistroPage(self.driver)
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def Registro_Cuenta(self, Cuenta_Info):
        try:
            self.driver.get(link_parabank)
            self.inicio_page.presionar_registro()
            self.registro_page.registrar_cuenta(Cuenta_Info)
        except Exception as e:
            self.logger.error(f"Se produjo un error durante el registro : {e}")

    def login(self, Cuenta_Info):
        try:
            self.login_page.iniciar_sesion(Cuenta_Info.username, Cuenta_Info.password)
        except Exception as e:
            self.logger.error(f"Se produjo un error al loguearse : {e}")

    def cerrar_sesion(self):
        try:
            self.inicio_page.cerrar_sesion()
        except Exception as e:
            self.logger.error(f"Se produjo un error al cerrar sesión : {e}")

    def valida_registro(self):
        try:
            return self.registro_page.valida_registro()
        except Exception as e:
            self.logger.error(f"Error durante la validación del registro: {e}")
            return False

    def valida_login(self):
        try:
            return self.login_page.valida_login()
        except Exception as e:
            self.logger.error(f"Error durante la validación del Login: {e}")
            return False

    def close(self):
        try:
            self.driver.quit()
        except Exception as e:
            self.logger.error(f"Se produjo un error al cerrar el driver : {e}")
