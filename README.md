# Prueba de Automatización con Python : Carlos Gamarra

## Requisitos

1. **Python**: Asegurarse de tener Pycharm Community Edition instalado.
2. **Entorno Virtual**: Instalar el intérprete de Python 3.12 o superior, luego crear un entorno virtual, Pycharm lo crea por defecto, pero para ello por cuestiones de comodidad instalar el intérprete de Python en el directorio :

    ```bash
    C:/Python312
    ```
   Luego al abrir proyecto indicará que hay un intérprete encontrado, este debe ser:
   ```bash
    C:/Python312/python.exe
    ```
   Elegir, aceptar y esperar que se instale (debe validar que se instale Python SDK en la carga de instalación al momento de aceptar - en la parte inferior del IDE se mostrarán unas barras cargando, allí podrá hacer seguimiento)

3. **Instalar Dependencias**:
   
   Pycharm lo suele detectar por defecto al momento de instalar el intérprete (se mostrará un mensaje "install requirements", dar click), pero manualmente se puede hacer desde la terminal ingresando el siguiente comando:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configuración del WebDriver**:

    - `chromedriver` se encuentra en `driver/chrome/chromedriver`.
    - Asegurarse que `chromedriver` no tenga la extensión de ejecutable.

        

## Ejecución

1. Para ejecutar el script principal, ir al archivo :

    ```bash
    main.py
    ```

## Adicionales

1. Ante errores de dependencias y packaging tools, ejecutar los siguientes comandos desde la terminal línea por línea:
   ```bash
   python -m ensurepip --upgrade
   pip install --upgrade pip setuptools
   python -m venv venv
   venv/Scripts/activate
    ```