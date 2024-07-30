import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import path_chromedriver, link_parabank
from DatosCuenta import InfoCuenta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class ParabankFlujo:
    def __init__(self):
        driver_chrome = Service(executable_path=path_chromedriver)
        self.driver = webdriver.Chrome(service=driver_chrome)
        self.espera = WebDriverWait(self.driver, 20)
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def esperar_elemento(self, by, value, reintentosBucles: int):
        """
        Espera hasta que el elemento mencionado sea visible en la página.

        Argumentos:
            by: Mecanismo de localización (por ejemplo, By.ID, By.XPATH, By.LINK_TEXT).
            value: Valor del localizador.
            reintentosBucles: Número máximo de intentos.

        Returns:
            True si el elemento es visible, caso contrario retornará False.
        """
        contador = 0
        while contador <= reintentosBucles:
            try:
                self.espera.until(EC.visibility_of_element_located((by, value)))
                self.logger.info(f"Elemento encontrado: {by} {value}")
                return True
            except TimeoutException:
                self.logger.info(f"Reintentando encontrar elemento: {by} {value}, intento {contador + 1}")
                time.sleep(2)
                contador += 1
        self.logger.error(f"Elemento no encontrado después de {reintentosBucles} reintentos: {by} {value}")
        return False

    def hacer_click(self, by, value, reintentosBucles=3):
        """
        Espera hasta que un elemento mencionado sea visible y luego hace clic en él.

        Argumentos:
            by: Mecanismo de localización (por ejemplo, By.ID, By.XPATH, By.LINK_TEXT).
            value: Valor del localizador.
            reintentosBucles: Número máximo de intentos.
        """
        try:
            if self.esperar_elemento(by, value, reintentosBucles):
                self.driver.find_element(by, value).click()
                self.logger.info(f"Clicked on element: {by} {value}")
            else:
                raise NoSuchElementException(f"No se pudo encontrar el elemento: {by} {value}")
        except Exception as e:
            self.logger.error(f"Error al hacer clic en el elemento: {by} {value}. Error: {e}")

    def enviar_texto(self, by, value, keys, reintentosBucles=3):
        """
        Espera hasta que un elemento sea visible y luego envía texto a él.

        Args:
            by: Mecanismo de localización (por ejemplo, By.ID).
            value: Valor del localizador.
            keys: Texto a enviar.
            reintentosBucles: Número máximo de intentos.
        """
        try:
            if self.esperar_elemento(by, value, reintentosBucles):
                self.driver.find_element(by, value).send_keys(keys)
                self.logger.info(f"Sent keys to element: {by} {value}")
            else:
                raise NoSuchElementException(f"No se pudo encontrar el elemento: {by} {value}")
        except Exception as e:
            self.logger.error(f"Error al enviar texto al elemento: {by} {value}. Error: {e}")

    def Registro_Cuenta(self, account_info: InfoCuenta):
        try:
            self.driver.get(link_parabank)
            self.hacer_click(By.LINK_TEXT, "Register")
            self.enviar_texto(By.ID, "customer.firstName", account_info.first_name)
            self.enviar_texto(By.ID, "customer.lastName", account_info.last_name)
            self.enviar_texto(By.ID, "customer.address.street", account_info.address)
            self.enviar_texto(By.ID, "customer.address.city", account_info.city)
            self.enviar_texto(By.ID, "customer.address.state", account_info.state)
            self.enviar_texto(By.ID, "customer.address.zipCode", account_info.zip_code)
            self.enviar_texto(By.ID, "customer.phoneNumber", account_info.phone)
            self.enviar_texto(By.ID, "customer.ssn", account_info.ssn)
            self.enviar_texto(By.ID, "customer.username", account_info.username)
            self.enviar_texto(By.ID, "customer.password", account_info.password)
            self.enviar_texto(By.ID, "repeatedPassword", account_info.password)

            self.hacer_click(By.XPATH, "//input[@value='Register']")
        except Exception as e:
            self.logger.error(f"Error during registration: {e}")

    def login(self, account_info: InfoCuenta):
        try:
            #self.driver.get(link_parabank)
            self.enviar_texto(By.NAME, "username", account_info.username)
            self.enviar_texto(By.NAME, "password", account_info.password)
            self.hacer_click(By.XPATH, "//input[@value='Log In']")
        except Exception as e:
            self.logger.error(f"Error during login: {e}")

    def cerrar_sesion(self):
        try:
            self.hacer_click(By.LINK_TEXT, "Log Out")
        except Exception as e:
            self.logger.error(f"Error al buscar : {e}")

    # def validate_login(self):
    #     try:
    #         return "Accounts Overview" in self.driver.page_source
    #     except Exception as e:
    #         self.logger.error(f"Error during login validation: {e}")
    #         return False

    def close(self):
        self.driver.quit()

    # def validate_registration(self):
    #     try:
    #         # Esperar a que el elemento sea visible
    #         if self.esperar_elemento(By.CSS_SELECTOR, "div#rightPanel p", 10):
    #             # Capturar el mensaje de éxito
    #             success_message_element = self.driver.find_element(By.CSS_SELECTOR, "div#rightPanel p")
    #             success_message = success_message_element.text
    #
    #             # Imprimir el mensaje capturado
    #             print(f"Mensaje capturado: {success_message}")
    #
    #             # Comparar el mensaje capturado con el mensaje esperado
    #             expected_message = "Your account was created successfully. You are now logged in."
    #             if expected_message in success_message:
    #                 self.logger.info("Registro exitoso. El mensaje coincide con el esperado.")
    #                 self.logger.info("Registro de cuenta completado")
    #                 return True
    #             else:
    #                 self.logger.error(f"Mensaje esperado no encontrado. Mensaje recibido: {success_message}")
    #                 return False
    #         else:
    #             self.logger.error("El elemento de mensaje de éxito no fue encontrado.")
    #             return False
    #     except Exception as e:
    #         self.logger.error(f"Error durante la validación del registro: {e}")
    #         return False

    def compare_element_text(self, by, value, expected_text, reintentos=10):
        """
        Compara el texto de un elemento con el texto esperado.

        Args:
            by: El tipo de selector (por ejemplo, By.CSS_SELECTOR).
            value: El valor del selector (por ejemplo, 'div#rightPanel p').
            expected_text: El texto esperado a comparar con el texto del elemento.
            reintentos: El número de reintentos para esperar a que el elemento sea visible.

        Returns:
            bool: True si el texto del elemento coincide con el texto esperado, False en caso contrario.
        """
        try:
            if self.esperar_elemento(by, value, reintentos):
                try:
                    element = self.driver.find_element(by, value)
                    actual_text = element.text
                    print(f"Mensaje capturado: {actual_text}")

                    if expected_text in actual_text:
                        self.logger.info(f"Texto coincide con el esperado: {expected_text}")
                        return True
                    else:
                        self.logger.error(f"Texto esperado no encontrado. Mensaje recibido: {actual_text}")
                        return False
                except Exception as e:
                    self.logger.error(f"Error al capturar el texto del elemento: {e}")
                    return False
            else:
                self.logger.error("El elemento no fue encontrado.")
                return False
        except Exception as e:
            self.logger.error(f"Error durante la comparación del texto del elemento: {e}")
            return False

    def validate_registration(self):
        """
        Valida el mensaje de éxito después del registro.

        Returns:
            bool: True si el mensaje coincide con el esperado, False en caso contrario.
        """
        try:
            expected_message = "Your account was created successfully. You are now logged in."
            return self.compare_element_text(By.CSS_SELECTOR, "div#rightPanel p", expected_message)

        except Exception as e:
            self.logger.error(f"Error durante la validación del registro: {e}")
            return False

    def validate_login(self):
        """
        Valida el mensaje después de iniciar sesión.

        Returns:
            bool: True si el mensaje coincide con el esperado, False en caso contrario.
        """
        try:
            expected_message = "Accounts Overview"
            return self.compare_element_text(By.CSS_SELECTOR, "h1",
                                             expected_message)
        except Exception as e:
            self.logger.error(f"Error durante la validación del Login: {e}")
            return False
