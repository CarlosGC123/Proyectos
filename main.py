import time
from Parabank import ParabankFlujo
from GeneradorCuenta import DatoAleatorio


def main():
    try:
        # Instanciando el flujo en una variable para interactuar con las clases
        flujo = ParabankFlujo()
        # Generamos información aleatoria y la encapsulamos
        info_cuenta = DatoAleatorio.GeneradorCuenta()
        # Mostrando la cuenta generada para registrar
        print("Datos de la cuenta generada para su registro:")
        print(info_cuenta)
        # Abrimos la página
        flujo.abrir_pagina()
        # Realizamos el registro de la cuenta almacenada
        flujo.registro_cuenta(info_cuenta)

        # Validación de registro completado
        if flujo.valida_registro():
            # Cerramos sesión
            flujo.cerrar_sesion()
            # Opción para navegar nuevamente en el link
            flujo.login(info_cuenta)

            # Validación de Login completado
            if flujo.valida_login():
                time.sleep(2)
                print("Login completado")
                input("Presiona Enter para cerrar el navegador...")
            else:
                print("Login fallido")
        else:
            print("El registro falló.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")


if __name__ == "__main__":
    main()
