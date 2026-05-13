from abc import ABC, abstractmethod
from excepciones import (
    ExcepcionServicioInvalido,
    ExcepcionServicioNoDisponible
)
from registro import registrar_error, registrar_informacion
class Servicio(ABC):
    """
    Clase abstracta que representa un servicio general del sistema.

    Esta clase define la estructura base para todos los servicios
    disponibles en el sistema SOFTWARE FJ.
    """
    def __init__(self, nombre, precio_base, disponible=True):
        """
        Inicializa un servicio base.
        Args:
            nombre (str): Nombre del servicio.
            precio_base (float): Precio base del servicio.
            disponible (bool, optional): Estado de disponibilidad.
        Raises:
            ExcepcionServicioInvalido:
                Si el nombre está vacío o el precio es inválido.
        """
        if not isinstance(nombre, str) or not nombre.strip():
            raise ExcepcionServicioInvalido(
                "El nombre del servicio no puede estar vacío"
            )

        if not isinstance(precio_base, (int, float)) or isinstance(precio_base, bool):
            raise ExcepcionServicioInvalido(
                "El precio base debe ser numérico"
            )

        if precio_base <= 0:
            raise ExcepcionServicioInvalido(
                "El precio base debe ser mayor a 0"
            )

        self._nombre = nombre.strip()
        self._precio_base = precio_base
        self._disponible = disponible

    def esta_disponible(self):
        """
        Verifica si el servicio se encuentra disponible.

        Returns:
            bool: Estado de disponibilidad.
        """
        return self._disponible

    def cambiar_disponibilidad(self, estado: bool):
        """
        Cambia el estado de disponibilidad del servicio.

        Args:
            estado (bool): Nuevo estado del servicio.
        """

        if not isinstance(estado, bool):
            raise ExcepcionServicioInvalido(
                "La disponibilidad debe ser un valor booleano"
            )
        self._disponible = estado

    @abstractmethod
    def calcular_costo(self, *args, **kwargs):
        """
        Calcula el costo total del servicio.

        Método abstracto que debe ser implementado
        por todas las clases hijas.
        """
        pass

    @abstractmethod
    def descripcion(self):
        """
        Retorna una descripción textual del servicio.

        Returns:
            str: Descripción del servicio.
        """
        pass


class ServicioSala(Servicio):
    """
    Servicio especializado para alquiler de salas.
    """
    def __init__(self, nombre, precio_base, horas):
        """
        Inicializa un servicio de sala.

        Args:
            nombre (str): Nombre de la sala.
            precio_base (float): Precio por hora.
            horas (int): Cantidad de horas reservadas.

        Raises:
            ExcepcionServicioInvalido:
                Si las horas son inválidas.
        """

        super().__init__(nombre, precio_base)

        if not isinstance(horas, int) or isinstance(horas, bool):
            raise ExcepcionServicioInvalido(
                "Las horas deben ser un número entero"
            )

        if horas <= 0:
            raise ExcepcionServicioInvalido(
                "Las horas deben ser mayores a 0"
            )

        if horas > 24:
            raise ExcepcionServicioInvalido(
                "Las horas no pueden superar 24"
            )

        self.horas = horas

    def calcular_costo(self, descuento=0):
        """
        Calcula el costo total del servicio de sala.

        Args:
            descuento (float, optional):
                Descuento aplicado al servicio.
                Debe estar entre 0 y 1.

        Returns:
            float: Costo total calculado.

        Raises:
            ExcepcionServicioNoDisponible:
                Si la sala no está disponible.

            ExcepcionServicioInvalido:
                Si el descuento es inválido.
        """

        try:

            if not self.esta_disponible():
                raise ExcepcionServicioNoDisponible(
                    "La sala no está disponible"
                )

            if not isinstance(descuento, (int, float)):
                raise ExcepcionServicioInvalido(
                    "El descuento debe ser numérico"
                )

            if descuento < 0 or descuento > 1:
                raise ExcepcionServicioInvalido(
                    "El descuento debe estar entre 0 y 1"
                )

            costo = self._precio_base * self.horas
            costo_final = costo - (costo * descuento)

            registrar_informacion(
                f"Cálculo sala: {costo_final}"
            )

            return costo_final

        except Exception as e:
            registrar_error(
                "Error al calcular costo de sala",
                e
            )
            raise

    def descripcion(self):
        """
        Genera una descripción del servicio.

        Returns:
            str: Descripción del servicio.
        """
        return f"Sala '{self._nombre}' por {self.horas} horas"

class ServicioEquipo(Servicio):
    """
    Servicio especializado para alquiler de equipos.
    """

    def __init__(self, nombre, precio_base, dias):
        """
        Inicializa un servicio de alquiler de equipos.

        Args:
            nombre (str): Nombre del equipo.
            precio_base (float): Precio base diario.
            dias (int): Cantidad de días.

        Raises:
            ExcepcionServicioInvalido:
                Si los días son inválidos.
        """

        super().__init__(nombre, precio_base)

        if not isinstance(dias, int) or isinstance(dias, bool):
            raise ExcepcionServicioInvalido(
                "Los días deben ser un número entero"
            )

        if dias <= 0:
            raise ExcepcionServicioInvalido(
                "Los días deben ser mayores a 0"
            )

        if dias > 365:
            raise ExcepcionServicioInvalido(
                "Los días no pueden superar 365"
            )

        self.dias = dias

    def calcular_costo(self, impuesto=0.19):
        """
        Calcula el costo total del servicio de equipo.

        Args:
            impuesto (float, optional):
                Impuesto aplicado al servicio.
                Debe estar entre 0 y 1.

        Returns:
            float: Costo total calculado.

        Raises:
            ExcepcionServicioNoDisponible:
                Si el equipo no está disponible.

            ExcepcionServicioInvalido:
                Si el impuesto es inválido.
        """

        try:

            if not self.esta_disponible():
                raise ExcepcionServicioNoDisponible(
                    "Equipo no disponible"
                )

            if not isinstance(impuesto, (int, float)):
                raise ExcepcionServicioInvalido(
                    "El impuesto debe ser numérico"
                )

            if impuesto < 0 or impuesto > 1:
                raise ExcepcionServicioInvalido(
                    "El impuesto debe estar entre 0 y 1"
                )

            costo = self._precio_base * self.dias
            costo_final = costo + (costo * impuesto)

            registrar_informacion(
                f"Cálculo equipo: {costo_final}"
            )

            return costo_final

        except Exception as e:
            registrar_error(
                "Error en cálculo de equipo",
                e
            )
            raise

    def descripcion(self):
        """
        Genera una descripción del servicio.

        Returns:
            str: Descripción del servicio.
        """
        return f"Equipo '{self._nombre}' por {self.dias} días"

class ServicioAsesoria(Servicio):
    """
    Servicio especializado para asesorías técnicas.
    """

    def __init__(self, nombre, precio_base, nivel):
        """
        Inicializa un servicio de asesoría.

        Args:
            nombre (str): Nombre de la asesoría.
            precio_base (float): Precio base.
            nivel (str): Nivel de complejidad.

        Raises:
            ExcepcionServicioInvalido:
                Si el nivel es inválido.
        """

        super().__init__(nombre, precio_base)

        niveles_validos = [
            "basico",
            "intermedio",
            "avanzado"
        ]

        if not isinstance(nivel, str):
            raise ExcepcionServicioInvalido(
                "El nivel debe ser texto"
            )

        if nivel.lower() not in niveles_validos:
            raise ExcepcionServicioInvalido(
                "Nivel de asesoría inválido"
            )

        self.nivel = nivel.lower()

    def calcular_costo(self, horas=1):
        """
        Calcula el costo total de la asesoría.

        Args:
            horas (int, optional):
                Cantidad de horas de asesoría.

        Returns:
            float: Costo total calculado.

        Raises:
            ExcepcionServicioNoDisponible:
                Si la asesoría no está disponible.

            ExcepcionServicioInvalido:
                Si las horas son inválidas.
        """

        try:

            if not self.esta_disponible():
                raise ExcepcionServicioNoDisponible(
                    "Asesoría no disponible"
                )

            if not isinstance(horas, int) or isinstance(horas, bool):
                raise ExcepcionServicioInvalido(
                    "Las horas deben ser un número entero"
                )

            if horas <= 0:
                raise ExcepcionServicioInvalido(
                    "Las horas deben ser mayores a 0"
                )

            if horas > 12:
                raise ExcepcionServicioInvalido(
                    "Las horas no pueden superar 12"
                )

            factor = 1

            if self.nivel == "intermedio":
                factor = 1.3

            elif self.nivel == "avanzado":
                factor = 1.6

            costo = self._precio_base * horas * factor

            registrar_informacion(
                f"Cálculo asesoría: {costo}"
            )

            return costo

        except Exception as e:
            registrar_error(
                "Error en asesoría",
                e
            )
            raise

    def descripcion(self):
        """
        Genera una descripción del servicio.

        Returns:
            str: Descripción del servicio.
        """
        return f"Asesoría '{self._nombre}' nivel {self.nivel}"  