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
    def __init__(
        self,
        cliente,
        servicio,
        fecha,
        duracion,
        estado="Pendiente"
    ):

        try:
            # Validación: el cliente debe ser un objeto de tipo Cliente
            if not isinstance(cliente, Cliente):
                raise ExcepcionReservaInvalida("Cliente inválido")

            # Validación: el servicio debe ser un objeto de tipo Servicio
            if not isinstance(servicio, Servicio):
                raise ExcepcionReservaInvalida("Servicio inválido")

            # Validación: la fecha no puede estar vacía
            if not fecha.strip():
                raise ExcepcionReservaInvalida(
                    "La fecha no puede estar vacía"
                )

            # Validación: la duración debe ser mayor a 0
            if duracion <= 0:
                raise ExcepcionReservaInvalida(
                    "La duración debe ser mayor a 0"
                )

            # Estados válidos de la reserva
            estados_validos = [
                "Pendiente",
                "Confirmada",
                "Cancelada"
            ]

            # Validación del estado
            if estado not in estados_validos:
                raise ExcepcionReservaInvalida(
                    "Estado de reserva inválido"
                )

            # Atributos de la reserva
            self.cliente = cliente
            self.servicio = servicio
            self.fecha = fecha
            self.duracion = duracion
            self.estado = estado

            # Registro de creación de reserva
            registrar_informacion(
                f"Reserva creada para "
                f"{self.cliente.obtener_nombre()}"
            )

        except Exception as e:

            # Registro del error ocurrido
            registrar_error("Error al crear reserva", e)

            # Encadenamiento de excepción
            raise ExcepcionReservaInvalida(
                "No fue posible crear la reserva"
            ) from e

        finally:
            # Mensaje final del proceso
            registrar_informacion(
                "Finaliza proceso de creación de reserva"
            )

    # Método para confirmar la reserva
    def confirmar_reserva(self):

        try:
            # Verificación del estado de la reserva
            if self.estado == "Cancelada":
                raise ExcepcionReservaInvalida(
                    "No se puede confirmar una reserva cancelada"
                )

            # Se calcula el costo del servicio
            costo = self.servicio.calcular_costo()

        except Exception as e:

            # Se registra el error ocurrido
            registrar_error("Error al confirmar reserva", e)

            # Se lanza una excepción personalizada
            raise ExcepcionReservaInvalida(
                "No fue posible realizar la reserva"
            ) from e

        else:
            # Cambio de estado de la reserva
            self.estado = "Confirmada"

            # Se registra la operación en el archivo log
            registrar_informacion(
                f"Reserva realizada para "
                f"{self.cliente.obtener_nombre()}"
            )

            # Mensaje de confirmación
            return f"""
Reserva confirmada
Cliente: {self.cliente.obtener_nombre()}
Servicio: {self.servicio.descripcion()}
Costo: {costo}
Fecha: {self.fecha}
Duración: {self.duracion}
Estado: {self.estado}
"""

        finally:
            # Registro final del proceso
            registrar_informacion(
                "Finaliza proceso de confirmación de reserva"
            )

    # Método para cancelar la reserva
    def cancelar_reserva(self):

        try:
            # Verificación del estado actual
            if self.estado == "Cancelada":
                raise ExcepcionReservaInvalida(
                    "La reserva ya fue cancelada"
                )

        except Exception as e:

            # Registro del error
            registrar_error("Error al cancelar reserva", e)

            # Encadenamiento de excepción
            raise ExcepcionReservaInvalida(
                "No fue posible cancelar la reserva"
            ) from e

        else:
            # Cambio de estado
            self.estado = "Cancelada"

            # Registro en logs
            registrar_informacion(
                f"Reserva cancelada para "
                f"{self.cliente.obtener_nombre()}"
            )

            return "Reserva cancelada correctamente"

        finally:
            # Registro final del proceso
            registrar_informacion(
                "Finaliza proceso de cancelación"
            )

    # Método para procesar la reserva
    def procesar_reserva(self):

        try:
            # Validación de disponibilidad del servicio
            if not self.servicio.esta_disponible():
                raise ExcepcionReservaInvalida(
                    "El servicio no está disponible"
                )

        except Exception as e:

            # Registro del error
            registrar_error("Error al procesar reserva", e)

            raise ExcepcionReservaInvalida(
                "No fue posible procesar la reserva"
            ) from e

        else:
            # Confirmación automática de la reserva
            return self.confirmar_reserva()

        finally:
            # Registro final del proceso
            registrar_informacion(
                "Finaliza proceso de reserva"
            )

    # Método para mostrar información de la reserva
    def mostrar_reserva(self):

        return f"""
Cliente: {self.cliente.obtener_nombre()}
Servicio: {self.servicio.descripcion()}
Fecha: {self.fecha}
Duración: {self.duracion}
Estado: {self.estado}
""" 