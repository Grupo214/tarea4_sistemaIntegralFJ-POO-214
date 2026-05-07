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

        # Validación: el cliente debe ser un objeto de tipo Cliente
        if not isinstance(cliente, Cliente):
            raise ExcepcionReservaInvalida("Cliente inválido")

        # Validación: el servicio debe ser un objeto de tipo Servicio
        if not isinstance(servicio, Servicio):
            raise ExcepcionReservaInvalida("Servicio inválido")

        # Validación: la fecha no puede estar vacía
        if not fecha.strip():
            raise ExcepcionReservaInvalida("La fecha no puede estar vacía")

        # Atributos de la reserva
        self.cliente = cliente
        self.servicio = servicio
        self.fecha = fecha

    # Método para confirmar la reserva
    def confirmar_reserva(self):

        try:
            # Se calcula el costo del servicio
            costo = self.servicio.calcular_costo()

            # Se registra la operación en el archivo log
            registrar_informacion(
                f"Reserva realizada para {self.cliente.get_nombre()}"
            )

            # Mensaje de confirmación
            return f"""
Reserva confirmada
Cliente: {self.cliente.get_nombre()}
Servicio: {self.servicio.descripcion()}
Costo: {costo}
Fecha: {self.fecha}
"""

        except Exception as e:

            # Se registra el error ocurrido
            registrar_error("Error al confirmar reserva", e)

            # Se lanza una excepción personalizada
            raise ExcepcionReservaInvalida(
                "No fue posible realizar la reserva"
            )

    # Método para mostrar información de la reserva
    def mostrar_reserva(self):

        return f"""
Cliente: {self.cliente.get_nombre()}
Servicio: {self.servicio.descripcion()}
Fecha: {self.fecha}
"""