#excepciones.py: Con excepciones perzonlalizadas para el sistema de SOFTWARE FJ

# Clase para errores en clientes
class ExcepcionClienteInvalido(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(mensaje)#llamada de constructor de la clase base Exception

 #Clase para reservas no validas
class ExcepcionReservaInvalida(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(mensaje)#llamada de constructor de la clase base Exception
        
#Clase para problemas con servicios       
class ExcepcionServicioInvalido(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(mensaje)#llamada de constructor de la clase base Exception
# Clase para servicios no disponibles
class ExcepcionServicioNoDisponible(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(mensaje)#llamada de constructor de la clase base Exception

# clase para operaciones no validas 
class ExcepcionOperacionInvalida(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(mensaje)#llamada de constructor de la clase base Exception