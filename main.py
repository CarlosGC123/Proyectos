# main.py

from Parabank import ParabankFlujo
from GeneradorCuenta import DatoAleatorio


def main():
    automator = ParabankFlujo()
    account_info = DatoAleatorio.generate_account()

    automator.register_account()
    if automator.validate_registration():
        print("Account registration successful.")
        automator.login()
        if automator.validate_login():
            print("Login successful.")
        else:
            print("Login failed.")
    else:
        print("Registration failed.")

    automator.close()


if __name__ == "__main__":
    main()
