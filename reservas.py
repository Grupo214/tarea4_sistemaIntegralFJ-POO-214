# Se importan las clases necesarias para crear una reserva
from cliente import Cliente
from servicio import Servicio

# Se importa la excepción personalizada para reservas inválidas
from excepciones import ExcepcionReservaInvalida

# Se importan funciones del sistema de registro
from registro import registrar_informacion, registrar_error


# Clase que representa una reserva dentro del sistema
class Reserva:
    """
    Representa una reserva realizada por un cliente para un servicio.

    La clase permite:
    - Validar los datos de una reserva.
    - Procesar reservas.
    - Cancelar reservas.
    - Mostrar la información almacenada.
    """

    # Constructor de la clase
    def __init__(self, cliente, servicio, fecha, duracion):
        """
        Inicializa una nueva reserva con los datos suministrados.

        Args:
            cliente (Cliente): Cliente asociado a la reserva.
            servicio (Servicio): Servicio reservado.
            fecha (str): Fecha programada para la reserva.
            duracion (int): Duración de la reserva en horas.

        Raises:
            ExcepcionReservaInvalida:
                Si alguno de los datos ingresados no es válido.
        """

        try:
            # Validación del cliente
            if not isinstance(cliente, Cliente):
                raise TypeError(
                    "El cliente suministrado no es un objeto válido de tipo Cliente"
                )

            # Validación del servicio
            if not isinstance(servicio, Servicio):
                raise TypeError(
                    "El servicio suministrado no es un objeto válido de tipo Servicio"
                )

            # Validación de la fecha
            if not isinstance(fecha, str) or not fecha.strip():
                raise ValueError("La fecha no puede estar vacía")

            # Validación de la duración
            if not isinstance(duracion, int):
                raise ValueError(
                    "La duración debe ser un número entero"
                )

            if duracion <= 0:
                raise ValueError(
                    "La duración debe ser mayor a 0"
                )

        except (TypeError, ValueError) as e:
            registrar_error(f"Error al crear reserva: {str(e)}", e)

            raise ExcepcionReservaInvalida(
                "Datos de reserva inválidos y/o insuficientes"
            ) from e

        else:
            # Asignación de atributos
            self.cliente = cliente
            self.servicio = servicio
            self.fecha = fecha.strip()
            self.estado = "Pendiente"
            self.duracion = duracion

            registrar_informacion(
                f"Reserva creada para {self.cliente.obtener_nombre()}"
            )

        finally:
            registrar_informacion(
                "Auditoría: Intento de creación de reserva finalizado"
            )

    # Método para procesar la reserva
    def procesar_reserva(self):
        """
        Procesa la reserva y calcula el costo del servicio.

        Returns:
            str: Mensaje con la información de la reserva confirmada.

        Raises:
            ExcepcionReservaInvalida:
                Si ocurre un error durante el procesamiento.
        """

        try:
            costo = self.servicio.calcular_costo()

        except Exception as e:
            registrar_error("Error al procesar reserva", e)

            raise ExcepcionReservaInvalida(
                "No fue posible realizar la reserva"
            ) from e

        else:
            self.estado = "Confirmada"

            registrar_informacion(
                f"Reserva confirmada para "
                f"{self.cliente.obtener_nombre()} "
                f"con costo: {costo}"
            )

            return (
                f"\nReserva Confirmada\n"
                f"Cliente: {self.cliente.obtener_nombre()}\n"
                f"Servicio: {self.servicio.descripcion()}\n"
                f"Duración: {self.duracion} horas\n"
                f"Estado: {self.estado}\n"
                f"Costo Total: {costo}\n"
                f"Fecha: {self.fecha}"
            )

        finally:
            print(
                "Auditoría: Proceso de confirmación de reserva finalizado."
            )

    # Método para cancelar la reserva
    def cancelar_reserva(self):
        """
        Cancela una reserva existente.

        Returns:
            str: Mensaje de confirmación de cancelación.

        Raises:
            ExcepcionReservaInvalida:
                Si la reserva ya se encuentra cancelada.
        """

        try:
            if self.estado == "Cancelada":
                raise ValueError(
                    "La reserva ya se encuentra cancelada."
                )

        except ValueError as e:
            registrar_error(
                "Error al cancelar: Reserva ya cancelada",
                e
            )

            raise ExcepcionReservaInvalida(
                "Operación no permitida"
            ) from e

        else:
            self.estado = "Cancelada"

            registrar_informacion(
                f"Reserva cancelada para "
                f"{self.cliente.obtener_nombre()}"
            )

            return (
                f"La reserva para "
                f"{self.cliente.obtener_nombre()} "
                f"ha sido cancelada exitosamente."
            )

        finally:
            print("Auditoría: Intento de cancelación procesado.")

    # Método para mostrar la información de la reserva
    def mostrar_reserva(self):
        """
        Retorna la información general de la reserva.

        Returns:
            str: Información completa de la reserva.
        """

        return (
            f"Cliente: {self.cliente.obtener_nombre()}, "
            f"Servicio: {self.servicio.descripcion()}, "
            f"Duración: {self.duracion} horas, "
            f"Estado: {self.estado}, "
            f"Fecha: {self.fecha}"
        )