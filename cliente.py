class Cliente:
    
    # Constructor de la clase
    # Se ejecuta cuando se crea un cliente
    def __init__(self, nombre, correo):
        
        # Atributos privados 
        self.__nombre = nombre 
        self.__correo = correo

        # Validación: el nombre no puede estar vacío
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        # Validación del correo
        if "@" not in correo or "." not in correo:
            raise ValueError("Correo inválido")
           

    # Método para obtener el nombre del cliente
    def get_nombre(self):
        return self.__nombre

    # Método para obtener el correo del cliente
    def get_correo(self):
        return self.__correo
    
    #Método para mostrar información
    def mostrar_info(self):
        return f"Cliente: {self.__nombre}, Correo: {self.__correo}"