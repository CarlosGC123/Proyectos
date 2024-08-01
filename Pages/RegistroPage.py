from .BasePage import BasePage
from selenium.webdriver.common.by import By

#Clase que contiene los métodos de registro de una cuenta


class RegistroPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def registrar_cuenta(self, cuenta_info):
        self.enviar_texto(By.ID, "customer.firstName", cuenta_info.first_name)
        self.enviar_texto(By.ID, "customer.lastName", cuenta_info.last_name)
        self.enviar_texto(By.ID, "customer.address.street", cuenta_info.address)
        self.enviar_texto(By.ID, "customer.address.city", cuenta_info.city)
        self.enviar_texto(By.ID, "customer.address.state", cuenta_info.state)
        self.enviar_texto(By.ID, "customer.address.zipCode", cuenta_info.zip_code)
        self.enviar_texto(By.ID, "customer.phoneNumber", cuenta_info.phone)
        self.enviar_texto(By.ID, "customer.ssn", cuenta_info.ssn)
        self.enviar_texto(By.ID, "customer.username", cuenta_info.username)
        self.enviar_texto(By.ID, "customer.password", cuenta_info.password)
        self.enviar_texto(By.ID, "repeatedPassword", cuenta_info.password)
        self.hacer_click(By.XPATH, "//input[@value='Register']")

    def valida_registro(self):
        mensaje = "Your account was created successfully. You are now logged in."
        return self.valida_texto_elemento(By.CSS_SELECTOR, "div#rightPanel p", mensaje)
