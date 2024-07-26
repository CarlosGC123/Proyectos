from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from config import path_chromedriver


class ParabankFlujo:
    def __init__(self):
        # Crear una instancia del servicio de ChromeDriver
        service = Service(executable_path=path_chromedriver)
        # Configurar el WebDriver
        self.driver = webdriver.Chrome(service=service)

    def register_account(self):
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        # Agrega el código para llenar el formulario y registrarse aquí...

    def validate_registration(self):
        success_message = self.driver.find_element(By.CSS_SELECTOR, "div#rightPanel p").text
        return "Your account was created successfully. You are now logged in." in success_message

    def login(self):
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        # Agrega el código para iniciar sesión aquí...

    def validate_login(self):
        return "Accounts Overview" in self.driver.page_source

    def close(self):
        self.driver.quit()
