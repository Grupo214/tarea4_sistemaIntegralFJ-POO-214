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
    def __init__(self, cliente, servicio, fecha, duracion):
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
            
            # Validación: la duración debe ser un número entero positivo
            if not isinstance(duracion, int) or duracion <= 0:
                raise ValueError("La duración debe ser un número entero positivo"
                                 )
        except (TypeError, ValueError) as e:
            registrar_error(f"Error al crear reserva: {str(e)}", e)
            raise ExcepcionReservaInvalida("Datos de reserva inválidos y/o insuficientes") from e
            
        else:
            # Asignación de los atributos de la reserva, solo si son validos
            self.cliente = cliente
            self.servicio = servicio
            self.fecha = fecha
            self.estado = "Pendiente"
            self.duracion = duracion
        # Auditoría: se registra el intento de creación de reserva, independientemente del resultado
        finally:
            registrar_informacion("Auditoria: Intento de creación de reserva finalizado")
    
    # Método para procesar la reserva, con manejo de excepciones para errores durante el cálculo del costo        
    def procesar_reserva(self):
        # Se intenta calcular el costo del servicio, si ocurre un error se registra y se lanza una excepción personalizada
        try:
            costo = self.servicio.calcular_costo()
            
        # Si el costo es negativo, se considera un error en la lógica del servicio y se lanza una excepción
        except Exception as e:
            registrar_error("Error al procesar reserva", e)
            raise ExcepcionReservaInvalida("No fue posible realizar la reserva") from e
        
        # Si el costo es negativo, se considera un error en la lógica del servicio y se lanza una excepción personalizada
        else:
            self.estado = "Confirmada"
            registrar_informacion(f"Reserva confirmada para {self.cliente.obtener_nombre()} con costo: {costo}")
            return f"\nReserva Confirmada\nCliente: {self.cliente.obtener_nombre()}\nServicio: {self.servicio.descripcion()}\nDuración: {self.duracion} horas\nEstado: {self.estado}\nCosto Total: {costo}\nFecha: {self.fecha}"
        finally:
            print("Auditoria: Proceso de confirmación de reserva finalizado.")
            
    # Método para cancelar la reserva, con validación de estado y manejo de excepciones
    def cancelar_reserva(self):
        # Se valida que la reserva no esté ya cancelada antes de cambiar su estado, si ya está cancelada se lanza una excepción personalizada
        try:
            if self.estado == "Cancelada":
                raise ValueError("La reserva ya se encuentra cancelada.")
            
        # Si ocurre un error durante la validación, se registra el error y se lanza una excepción personalizada para indicar que la operación no es permitida
        except ValueError as e:
            registrar_error("Error al cancelar: Reserva ya cancelada", e)
            raise ExcepcionReservaInvalida("Operación no permitida") from e
        
        # Si la reserva no está cancelada, se procede a cambiar su estado a "Cancelada" y se registra la información de la cancelación
        else:
            self.estado = "Cancelada"
            registrar_informacion(f"Reserva cancelada para {self.cliente.obtener_nombre()}")
            return f"La reserva para {self.cliente.obtener_nombre()} ha sido cancelada exitosamente."
        finally:
            print("Auditoria: Intento de cancelación procesado.")

    # Método para mostrar la información de la reserva
    def mostrar_reserva(self):
        return f"Cliente: {self.cliente.obtener_nombre()}, Servicio: {self.servicio.descripcion()}, Duración: {self.duracion} horas, Estado: {self.estado}, Fecha: {self.fecha}"
