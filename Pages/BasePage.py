import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

#Clase que contiene los métodos principales con los que interactuarán los elementos


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.espera = WebDriverWait(self.driver, 50)
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def esperar_carga_pagina(self, timeout=100):
        """
        Método que espera hasta que la página se cargue completamente.

        Argumentos:
            timeout: Tiempo máximo de espera en segundos.

        Returns:
            True si la página se carga completamente dentro del tiempo, False en caso contrario.
        """
        try:
            self.logger.info("Abriendo página Parabank...")
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
            self.logger.info("Página cargada completamente.")
            return True
        except TimeoutException:
            self.logger.error("La página no se cargó completamente.")
            return False

    def esperar_elemento(self, by, elemento, reintentosBucles: int):
        """
        Método que espera hasta que el elemento mencionado sea visible en la página.

        Argumentos:
            by: Mecanismo de localización (por ejemplo, By.ID, By.XPATH, By.LINK_TEXT).
            elemento: Localizador del elemento a buscar.
            reintentosBucles: Número máximo de intentos.
        Returns:
               True si el elemento es visible, caso contrario retornará False.
        """
        contador = 0
        while contador <= reintentosBucles:
            try:
                self.logger.info(f"Buscando elemento...{elemento}")
                self.espera.until(EC.visibility_of_element_located((by, elemento)))
                self.logger.info(f"Elemento encontrado: {by} {elemento}")
                return True
            except TimeoutException:
                self.logger.info(f"Reintentando encontrar elemento: {by} - {elemento}, intento {contador + 1}")
                contador += 1
        self.logger.error(f"Elemento no encontrado después de {reintentosBucles} reintentos: {by} - {elemento} - ERROR")
        return False

    def hacer_click(self, by, elemento, reintentosBucles=3):
        """
        Método que espera hasta que un elemento mencionado sea visible y luego hace clic en él.

        Argumentos:
            by: Mecanismo de localización (por ejemplo, By.ID, By.XPATH, By.LINK_TEXT).
            elemento : Localizador del elemento a hacer click
            reintentosBucles: Número máximo de intentos.
        """
        try:
            if self.esperar_elemento(by, elemento, reintentosBucles):
                self.driver.find_element(by, elemento).click()
                self.logger.info(f"Se dió click en el elemento : {by} - {elemento}")
            else:
                raise NoSuchElementException(f"No se pudo encontrar el elemento: {by} - {elemento}")
        except Exception as e:
            self.logger.error(f"Error al hacer clic en el elemento: {by} - {elemento}. Error: {e}")

    def enviar_texto(self, by, elemento, texto, reintentosBucles=3):
        """
        Método que espera hasta que un elemento sea visible y luego envía texto a él.

        Argumentos:
            by: Mecanismo de localización (por ejemplo, By.ID).
            elemento: Localizador del elemento.
            texto: Texto a enviar.
            reintentosBucles: Número máximo de intentos.
        """
        try:
            if self.esperar_elemento(by, elemento, reintentosBucles):
                self.driver.find_element(by, elemento).send_keys(texto)
                self.logger.info(f"Se escribió en el elemento : {by} - {elemento}")
            else:
                raise NoSuchElementException(f"No se pudo encontrar el elemento: {by} - {elemento}")
        except Exception as e:
            self.logger.error(f"Error al enviar texto al elemento: {by} - {elemento}. Error: {e}")

    def valida_texto_elemento(self, by, elemento, texto, reintentos=10):
        """
        Método que compara el texto de un elemento con el texto esperado.

        Argumentos:
            by: El tipo de selector (por ejemplo, By.CSS_SELECTOR).
            elemento: Localizador del elemento.
            texto: El texto esperado que se comparará con el texto del elemento.
            reintentos: El número de reintentos para esperar a que el elemento sea visible.

        Returns:
            bool: True si el texto del elemento coincide con el texto esperado, False en caso contrario.
        """
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
                        self.logger.error(f"Texto capturado no coincide. Texto capturado : {texto_capturado} - VALIDACIÓN INCORRECTA")
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

