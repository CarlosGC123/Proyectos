import logging
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

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

    def Abrir_Pagina(self):
        #Flujo de carga de la página de Parabank
        try:
            self.logger.info(f"Inicializando flujo Parabank...")
            self.driver.get(link_parabank)
            self.inicio_page.esperar_carga_pagina()
        except Exception as e:
            self.logger.error(f"Error con la carga completa de la página : {e}")

    def Registro_Cuenta(self, Cuenta_Info):
        #Flujo para Registrar una Cuenta de Parabank
        try:
            self.logger.info(f"Registro de Cuenta generada")
            self.inicio_page.presionar_registro()
            self.registro_page.registrar_cuenta(Cuenta_Info)
        except Exception as e:
            self.logger.error(f"Error durante el registro : {e}")

    def login(self, Cuenta_Info):
        #Flujo para iniciar sesión con una cuenta creada
        try:
            self.logger.info(f"Iniciando sesión...")
            self.login_page.iniciar_sesion(Cuenta_Info.username, Cuenta_Info.password)
        except Exception as e:
            self.logger.error(f"Error al hacer login : {e}")

    def cerrar_sesion(self):
        #Flujo para cerrar sesión de una cuenta previamente logueada
        try:
            self.logger.info(f"Cerrando sesión...")
            self.inicio_page.cerrar_sesion()
        except Exception as e:
            self.logger.error(f"Error al cerrar sesión : {e}")

    def valida_registro(self):
        #Flujo para validar el registro exitoso de una cuenta
        try:
            self.logger.info(f"Validando registros de cuenta...")
            return self.registro_page.valida_registro()
        except Exception as e:
            self.logger.error(f"Error durante la validación del registro: {e}")
            return False

    def valida_login(self):
        #Flujo para validar login exitoso de una cuenta
        try:
            self.logger.info(f"Validando login....")
            return self.login_page.valida_login()
        except Exception as e:
            self.logger.error(f"Error durante la validación del Login: {e}")
            return False

    def close(self):
        #Flujo para cerrar el navegador
        try:
            self.logger.info(f"Cerrando navegador...")
            self.driver.quit()
        except Exception as e:
            self.logger.error(f"Error al cerrar el driver : {e}")
