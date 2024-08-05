import time
from Parabank import ParabankFlujo
from GeneradorCuenta import DatoAleatorio


def main():
    try:
        #Instanciando el flujo en una variable para interactuar con las clases
        Flujo = ParabankFlujo()
        #Generamos información aleatoria y la encapsulamos
        Info_Cuenta = DatoAleatorio.GeneradorCuenta()
        #Mostrando la cuenta generada para registrar
        print("Datos de la cuenta generada para su registro:")
        print(Info_Cuenta)
        #Abrimos la página
        Flujo.Abrir_Pagina()
        #Realizamos el registro de la cuenta almacenada
        Flujo.Registro_Cuenta(Info_Cuenta)

        #Validación de registro completado
        if Flujo.valida_registro():
            #Cerramos sesión
            Flujo.cerrar_sesion()
            #Opción para navegar nuevamente en el link
            Flujo.login(Info_Cuenta)

            #Validación de Login completado
            if Flujo.valida_login():
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

