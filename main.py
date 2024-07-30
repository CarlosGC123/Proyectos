import time
from Parabank import ParabankFlujo
from GeneradorCuenta import DatoAleatorio


def main():
    try:
        automator = ParabankFlujo()
        account_info = DatoAleatorio.generate_account()
        automator.Registro_Cuenta(account_info)

        if automator.validate_registration():
            automator.cerrar_sesion()
            automator.login(account_info)

            if automator.validate_login():
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
