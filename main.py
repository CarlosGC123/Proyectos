import time
from Parabank import ParabankFlujo
from GeneradorCuenta import DatoAleatorio


def main():
    try:
        automator = ParabankFlujo()
        account_info = DatoAleatorio.GeneradorCuenta()
        automator.Registro_Cuenta(account_info)

        if automator.valida_registro():
            automator.cerrar_sesion()
            automator.login(account_info)

            if automator.valida_login():
                time.sleep(2)
                print("Login completado")
            else:
                print("Login fallido")
        else:
            print("El registro falló.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")


if __name__ == "__main__":
    main()

