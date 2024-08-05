import random
import string
from DatosCuenta import InfoCuenta

#Clase que genera información aleatoria para instanciar en la clase InfoCuenta


class DatoAleatorio:
    def __init__(self):
        pass

    @staticmethod
    def GeneradorCuenta():
        return InfoCuenta(
            first_name=''.join(random.choices(string.ascii_letters, k=6)),
            last_name=''.join(random.choices(string.ascii_letters, k=6)),
            address=''.join(random.choices(string.ascii_letters + string.digits, k=10)),
            city=''.join(random.choices(string.ascii_letters, k=5)),
            state=''.join(random.choices(string.ascii_letters, k=2)),
            zip_code=''.join(random.choices(string.digits, k=5)),
            phone=''.join(random.choices(string.digits, k=10)),
            ssn=''.join(random.choices(string.digits, k=9)),
            username=''.join(random.choices(string.ascii_letters + string.digits, k=8)),
            password=''.join(random.choices(string.ascii_letters + string.digits, k=12))
        )
