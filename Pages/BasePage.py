import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.espera = WebDriverWait(self.driver, 50)
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def esperar_elemento(self, by, elemento, reintentosBucles: int):
        contador = 0
        while contador <= reintentosBucles:
            try:
                self.espera.until(EC.visibility_of_element_located((by, elemento)))
                self.logger.info(f"Elemento encontrado: {by} {elemento}")
                return True
            except TimeoutException:
                self.logger.info(f"Reintentando encontrar elemento: {by} {elemento}, intento {contador + 1}")
                contador += 1
        self.logger.error(f"Elemento no encontrado después de {reintentosBucles} reintentos: {by} {elemento}")
        return False

    def hacer_click(self, by, elemento, reintentosBucles=3):
        try:
            if self.esperar_elemento(by, elemento, reintentosBucles):
                self.driver.find_element(by, elemento).click()
                self.logger.info(f"Se dió click en el elemento : {by} {elemento}")
            else:
                raise NoSuchElementException(f"No se pudo encontrar el elemento: {by} {elemento}")
        except Exception as e:
            self.logger.error(f"Se produjo un error al hacer clic en el elemento: {by} {elemento}. Error: {e}")

    def enviar_texto(self, by, elemento, texto, reintentosBucles=3):
        try:
            if self.esperar_elemento(by, elemento, reintentosBucles):
                self.driver.find_element(by, elemento).send_keys(texto)
                self.logger.info(f"Se escribió en el elemento : {by} {elemento}")
            else:
                raise NoSuchElementException(f"No se pudo encontrar el elemento: {by} {elemento}")
        except Exception as e:
            self.logger.error(f"Se produjo un error al enviar texto al elemento: {by} {elemento}. Error: {e}")

    def valida_texto_elemento(self, by, elemento, texto, reintentos=10):
        try:
            if self.esperar_elemento(by, elemento, reintentos):
                try:
                    element = self.driver.find_element(by, elemento)
                    texto_capturado = element.text
                    self.logger.info(f"Contenido del texto capturado : {texto_capturado}")

                    if texto in texto_capturado:
                        self.logger.info(f"Texto coincide con el capturado: {texto}")
                        return True
                    else:
                        self.logger.error(f"Texto capturado no coincide. Texto capturado : {texto_capturado}")
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

