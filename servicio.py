from abc import ABC, abstractmethod # Se importan ABC Abstract Base Class y abstractmethod desde el módulo abc.
# Esto permite crear clases que no se pueden usar directamente, 
# sino que sirven como base para crear otras clases.
from excepciones import ExcepcionServicioInvalido, ExcepcionServicioNoDisponible
# Se importan las excepciones personalizadas definidas en el sistema.
# Estas excepciones permiten manejar errores de forma más específica y controlada.
from registro import registrar_error, registrar_informacion
# Se importan funciones del sistema de registro (logs).
# Estas funciones permiten guardar información y errores en un archivo.

class Servicio(ABC):
# Esta clase representa una entidad general del sistema.
# Al ser abstracta, no se puede crear un objeto directamente a partir de ella.
# Su propósito es definir una estructura común para todos los servicios.

    def __init__(self, nombre, precio_base, disponible=True):  # Constructor de la clase

        if not nombre or not nombre.strip(): # Validación: el nombre no puede estar vacío ni contener solo espacios
            raise ExcepcionServicioInvalido("El nombre del servicio no puede estar vacío")

        if precio_base <= 0: # Validación: el precio base debe ser mayor a 0
            raise ExcepcionServicioInvalido("El precio base debe ser mayor a 0")

        self._nombre = nombre
        self._precio_base = precio_base
        self._disponible = disponible
         # Atributos protegidos (se pueden acceder desde clases hijas)   

    def esta_disponible(self):  # Método que indica si el servicio está disponible
        return self._disponible

    def cambiar_disponibilidad(self, estado: bool): # Método que permite cambiar el estado de disponibilidad del servicio
        self._disponible = estado

    @abstractmethod  # Método abstracto: obliga a las clases hijas a implementar su propia lógica
    def calcular_costo(self, *args, **kwargs):
        pass

    @abstractmethod  # Método abstracto para describir el servicio
    def descripcion(self):
        pass

class ServicioSala(Servicio):
# Clase que representa el servicio de alquiler de salas.
# Hereda de la clase abstracta Servicio. 

    def __init__(self, nombre, precio_base, horas):
        super().__init__(nombre, precio_base)  # Se llama al constructor de la clase padre

        if horas <= 0: # Validación: las horas deben ser mayores a 0
            raise ExcepcionServicioInvalido("Las horas deben ser mayores a 0")

        self.horas = horas # Atributo específico de esta clase

    def calcular_costo(self, descuento=0): # Implementación del método calcular_costo
        try:
            if not self.esta_disponible(): # Verificación de disponibilidad del servicio
                raise ExcepcionServicioNoDisponible("La sala no está disponible")

            costo = self._precio_base * self.horas   # Cálculo del costo base
            costo_final = costo - (costo * descuento)  # Aplicación de descuento

            registrar_informacion(f"Cálculo sala: {costo_final}")  # Registro del cálculo en el sistema de logs
            return costo_final

        except Exception as e:
            registrar_error("Error al calcular costo de sala", e)  # Registro del error en caso de excepción
            raise

    def descripcion(self): # Método que devuelve una descripción del servicio
        return f"Sala '{self._nombre}' por {self.horas} horas"



class ServicioEquipo(Servicio): 
    # Clase que representa el servicio de alquiler de equipos. 

    def __init__(self, nombre, precio_base, dias):
        super().__init__(nombre, precio_base)

        if dias <= 0: # Validación: los días deben ser mayores a 0
            raise ExcepcionServicioInvalido("Los días deben ser mayores a 0")

        self.dias = dias

    def calcular_costo(self, impuesto=0.19):
        try:
            if not self.esta_disponible():  # Verificación de disponibilidad
                raise ExcepcionServicioNoDisponible("Equipo no disponible")

            costo = self._precio_base * self.dias # Cálculo del costo base
            costo_final = costo + (costo * impuesto) # Aplicación de impuesto

            registrar_informacion(f"Cálculo equipo: {costo_final}")  # Registro en logs
            return costo_final

        except Exception as e:
            registrar_error("Error en cálculo de equipo", e)
            raise

    def descripcion(self):
        return f"Equipo '{self._nombre}' por {self.dias} días"


class ServicioAsesoria(Servicio): 
# Clase que representa el servicio de asesorías especializadas.

    def __init__(self, nombre, precio_base, nivel):
        super().__init__(nombre, precio_base)

        niveles_validos = ["basico", "intermedio", "avanzado"] # Lista de niveles válidos

        if nivel.lower() not in niveles_validos: # Validación del nivel ingresado
            raise ExcepcionServicioInvalido("Nivel de asesoría inválido")

        self.nivel = nivel.lower()  # Se almacena el nivel en minúscula para evitar inconsistencias

    def calcular_costo(self, horas=1):
        try:
            if not self.esta_disponible(): # Verificación de disponibilidad
                raise ExcepcionServicioNoDisponible("Asesoría no disponible")

            factor = 1 
            if self.nivel == "intermedio":
                factor = 1.3
            elif self.nivel == "avanzado":
                factor = 1.6
            # Definición de factor según el nivel

            costo = self._precio_base * horas * factor  # Cálculo del costo total

            registrar_informacion(f"Cálculo asesoría: {costo}")  # Registro del cálculo
            return costo

        except Exception as e:
            registrar_error("Error en asesoría", e)
            raise

    def descripcion(self):
        return f"Asesoría '{self._nombre}' nivel {self.nivel}" 