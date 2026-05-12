# Se importan las clases necesarias para crear una reserva
from cliente import Cliente
from servicio import Servicio

# Se importa la excepción personalizada para reservas inválidas
from excepciones import ExcepcionReservaInvalida

# Se importan funciones del sistema de registro
from registro import registrar_informacion, registrar_error


# Clase que representa una reserva dentro del sistema
class Reserva:

    # Constructor de la clase
    def __init__(self, cliente, servicio, fecha):
        try:
            # Validación: el cliente debe ser un objeto de tipo Cliente
            if not isinstance(cliente, Cliente):
                raise TypeError("El cliente suministrado no es un objeto válido de tipo Cliente")
            # Validación: el servicio debe ser un objeto de tipo Servicio
            if not isinstance(servicio, Servicio):
                raise TypeError("El servicio suministrado no es un objeto válido de tipo Servicio")

            # Validación: la fecha no puede estar vacía
            if not fecha.strip():
                raise ValueError("La fecha no puede estar vacía")

        except (TypeError, ValueError) as e:
            registrar_error(f"Error al crear reserva: {str(e)}", e)
            raise ExcepcionReservaInvalida("Datos de reserva inválidos y/o insuficientes") from e
            
        else:
            # Asignación de los atributos de la reserva, solo si son validos
            self.cliente = cliente
            self.servicio = servicio
            self.fecha = fecha
            
        # Auditoría: se registra el intento de creación de reserva, independientemente del resultado
        finally:
            registrar_informacion("Auditoria: Intento de creación de reserva finalizado")
            
    # Método para confirmar la reserva
    def confirmar_reserva(self):
        # Se intenta confirmar la reserva y calcular el costo del servicio
        try:
            # Se calcula el costo del servicio
            costo = self.servicio.calcular_costo()

        # Si ocurre cualquier excepción durante el proceso de confirmación, este se captura y maneja 
        except Exception as e:

            # Se registra el error ocurrido
            registrar_error("Error al confirmar reserva", e)
            # Se lanza una excepción personalizada
            raise ExcepcionReservaInvalida("No fue posible realizar la reserva") from e
        # Si no hubo errores, se confirma la reserva
        else:
            # Se registra la confirmación exitosa de la reserva
            registrar_informacion(f"Reserva confirmada para {self.cliente.obtener_nombre()} con costo: {costo}")
            return f"""
Reserva confirmada para {self.cliente.obtener_nombre()} con costo: {costo}
cliente: {self.cliente.obtener_nombre()}
servicio: {self.servicio.descripcion()}
costo: {costo}
fecha: {self.fecha}
"""
        # Auditoría: se registra la finalización del proceso de confirmación de reserva, independientemente del resultado
        finally:
            print(f"Auditoria:Proceso de confirmación de reserva finalizado para {self.cliente.obtener_nombre()}")
            
    # Método para mostrar información de la reserva
    def mostrar_reserva(self):

        return f"""
Cliente: {self.cliente.obtener_nombre()}
Servicio: {self.servicio.descripcion()}
Fecha: {self.fecha}
"""