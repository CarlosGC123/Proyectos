#Clase para el almacenamiento de información de una cuenta

class InfoCuenta:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, ssn, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.ssn = ssn
        self.username = username
        self.password = password

    def __str__(self):
        return (f"Nombre: {self.first_name} {self.last_name}\n"
                f"Dirección: {self.address}, {self.city}, {self.state} {self.zip_code}\n"
                f"Teléfono: {self.phone}\n"
                f"SSN: {self.ssn}\n"
                f"Usuario: {self.username}\n"
                f"Contraseña: {self.password}")
