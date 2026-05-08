# Se importa el registro para registrar eventos relacionados con errores e información del cliente
from registro import registrar_error, registrar_informacion
# Se importa la excepción personalizada para manejar errores específicos de cliente
from excepciones import ExcepcionClienteInvalido

# Clase Cliente que representa a un cliente y sus datos en el sistema
class Cliente:
    
    # Constructor de la clase
    # Se ejecuta cuando se crea un cliente
    def __init__(self, nombre, correo, telefono):

        try:
            if not nombre or not correo or not telefono:
                raise ExcepcionClienteInvalido("Nombre, correo y teléfono son obligatorios")
            # validación de los datos del cliente
            self._validar_nombre (nombre)
            self._validar_correo (correo)
            self._validar_telefono (telefono)
            
            # registro de los datos del cliente
            self.__nombre = nombre.strip()
            self.__correo = correo.strip()
            self.__telefono = telefono.strip() 
            registrar_informacion(f"Cliente creado: {self.__nombre} ({self.__correo}, {self.__telefono})")
            
        except ExcepcionClienteInvalido as e:
            registrar_error(f"Error al crear cliente: {str(e)}", e)
            raise
        
    # Metodo privado para validar el nombre del cliente
    def _validar_nombre(self, nombre):
        # Valida el nombre del cliente
        if not nombre or not nombre.strip():
            raise ExcepcionClienteInvalido("El nombre del cliente no puede estar vacío")
        if len(nombre.strip()) < 3:
            raise ExcepcionClienteInvalido("El nombre del cliente debe tener al menos 3 caracteres")
        
    # Metodo privado para validar el correo del cliente        
    def _validar_correo(self, correo):
        # Valida el correo del cliente
        if not correo or not correo.strip():
            raise ExcepcionClienteInvalido("El correo del cliente no puede estar vacío")
        if "@" not in correo or "." not in correo:
            raise ExcepcionClienteInvalido("El correo del cliente no es válido")
        

    # Metodo privado para validar el teléfono del cliente
    def _validar_telefono(self, telefono):
        # Valida el teléfono del cliente
        if not telefono or not telefono.strip():
            raise ExcepcionClienteInvalido("El teléfono del cliente no puede estar vacío")
        if not telefono.replace(" ", "").isdigit() or len(telefono.strip()) < 7:
            raise ExcepcionClienteInvalido("El teléfono del cliente no es válido")
        
    
    # Metodos para obtener los datos del cliente
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_correo(self):
        return self.__correo

    def obtener_telefono(self):
        return self.__telefono
    
    # Metodo para mostrar la información del cliente:
    def mostrar_informacion(self):
        return f"Cliente: {self.__nombre}, Correo: {self.__correo}, Teléfono: {self.__telefono}"