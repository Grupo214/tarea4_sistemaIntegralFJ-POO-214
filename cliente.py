# Se importa el registro para registrar eventos relacionados con errores e información del cliente
from registro import registrar_error, registrar_informacion

# Se importa la excepción personalizada para manejar errores específicos de cliente
from excepciones import ExcepcionClienteInvalido


# Clase Cliente que representa a un cliente dentro del sistema
class Cliente:

    """
    Clase que representa un cliente del sistema SOFTWARE FJ.

    Permite almacenar y validar la información personal del cliente,
    incluyendo nombre, correo electrónico y teléfono.
    """

    # Constructor de la clase
    def __init__(self, nombre, correo, telefono):

        """
        Inicializa un nuevo cliente con sus datos básicos.

        Args:
            nombre (str): Nombre completo del cliente.
            correo (str): Correo electrónico del cliente.
            telefono (str): Número telefónico del cliente.

        Raises:
            ExcepcionClienteInvalido:
                Si alguno de los datos suministrados no es válido.
        """

        try:

            # Validación de datos obligatorios
            if not nombre or not correo or not telefono:
                raise ExcepcionClienteInvalido(
                    "Nombre, correo y teléfono son obligatorios"
                )

            # Validaciones individuales
            self._validar_nombre(nombre)
            self._validar_correo(correo)
            self._validar_telefono(telefono)

            # Registro de atributos privados
            self.__nombre = nombre.strip()
            self.__correo = correo.strip().lower()
            self.__telefono = telefono.strip()

            registrar_informacion(
                f"Cliente creado: {self.__nombre} "
                f"({self.__correo}, {self.__telefono})"
            )

        except ExcepcionClienteInvalido as e:

            registrar_error(
                f"Error al crear cliente: {str(e)}",
                e
            )

            raise

    # Método privado para validar el nombre
    def _validar_nombre(self, nombre):

        """
        Valida el nombre del cliente.

        Args:
            nombre (str): Nombre ingresado.

        Raises:
            ExcepcionClienteInvalido:
                Si el nombre está vacío, es muy corto
                o contiene caracteres inválidos.
        """

        if not nombre or not nombre.strip():
            raise ExcepcionClienteInvalido(
                "El nombre del cliente no puede estar vacío"
            )

        nombre = nombre.strip()

        if len(nombre) < 3:
            raise ExcepcionClienteInvalido(
                "El nombre del cliente debe tener al menos 3 caracteres"
            )

        # Permite letras y espacios únicamente
        if not nombre.replace(" ", "").isalpha():
            raise ExcepcionClienteInvalido(
                "El nombre solo debe contener letras"
            )

    # Método privado para validar el correo
    def _validar_correo(self, correo):

        """
        Valida el correo electrónico del cliente.

        Args:
            correo (str): Correo electrónico ingresado.

        Raises:
            ExcepcionClienteInvalido:
                Si el correo no cumple con un formato válido.
        """

        if not correo or not correo.strip():
            raise ExcepcionClienteInvalido(
                "El correo del cliente no puede estar vacío"
            )

        correo = correo.strip()

        if "@" not in correo or "." not in correo:
            raise ExcepcionClienteInvalido(
                "El correo del cliente no es válido"
            )

        if correo.startswith("@") or correo.endswith("@"):
            raise ExcepcionClienteInvalido(
                "El correo del cliente no es válido"
            )

    # Método privado para validar el teléfono
    def _validar_telefono(self, telefono):

        """
        Valida el número telefónico del cliente.

        Args:
            telefono (str): Número telefónico ingresado.

        Raises:
            ExcepcionClienteInvalido:
                Si el teléfono contiene caracteres inválidos
                o no cumple la longitud mínima requerida.
        """

        if not telefono or not telefono.strip():
            raise ExcepcionClienteInvalido(
                "El teléfono del cliente no puede estar vacío"
            )

        telefono_limpio = telefono.replace(" ", "").strip()

        if not telefono_limpio.isdigit():
            raise ExcepcionClienteInvalido(
                "El teléfono solo debe contener números"
            )

        if len(telefono_limpio) < 7 or len(telefono_limpio) > 15:
            raise ExcepcionClienteInvalido(
                "El teléfono del cliente no es válido"
            )

    # Métodos getters
    def obtener_nombre(self):

        """
        Retorna el nombre del cliente.

        Returns:
            str: Nombre del cliente.
        """

        return self.__nombre

    def obtener_correo(self):

        """
        Retorna el correo electrónico del cliente.

        Returns:
            str: Correo del cliente.
        """

        return self.__correo

    def obtener_telefono(self):

        """
        Retorna el número telefónico del cliente.

        Returns:
            str: Teléfono del cliente.
        """

        return self.__telefono

    # Método para mostrar información del cliente
    def mostrar_informacion(self):

        """
        Retorna una representación textual del cliente.

        Returns:
            str: Información general del cliente.
        """

        return (
            f"Cliente: {self.__nombre}, "
            f"Correo: {self.__correo}, "
            f"Teléfono: {self.__telefono}"
        )