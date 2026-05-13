from cliente import Cliente
from servicio import (
    # Se importan las clases principales que se van a usar en el sistema
    ServicioSala,
    ServicioEquipo,
    ServicioAsesoria
)
from reservas import Reserva

from excepciones import (
    # Se importan las excepciones personalizadas del sistema
    ExcepcionClienteInvalido,
    ExcepcionServicioInvalido,
    ExcepcionReservaInvalida,
    ExcepcionServicioNoDisponible
)

# Se importa la función para registrar información en logs
from registro import registrar_informacion


# Listas donde se almacenan los objetos creados durante la ejecución
clientes = []
servicios = []
reservas = []

print("SOFTWARE FJ\n")  # Mensaje inicial del sistema


# OPERACIÓN 1
# Se intenta crear un cliente válido
try:

    cliente1 = Cliente(
        "Laura Medina",
        "laura.medina@gmail.com",
        "3204567812"
    )

    # Se guarda el cliente en la lista
    clientes.append(cliente1)

    print("Cliente registrado correctamente")
    print(cliente1.mostrar_informacion())

except ExcepcionClienteInvalido as e:

    # Se muestra el error si los datos son inválidos
    print(f"Error en cliente: {e}")

finally:

    # Mensaje final de la operación
    print("Finaliza operación 1\n")


# OPERACIÓN 2
# Se intenta crear un cliente con datos incorrectos
try:

    cliente2 = Cliente(
        "",
        "correoincorrecto",
        "12"
    )

    clientes.append(cliente2)

except ExcepcionClienteInvalido as e:

    print(f"Error en cliente: {e}")

finally:

    print("Finaliza operación 2\n")


# OPERACIÓN 3
# Se crea un servicio de sala válido
try:

    sala1 = ServicioSala(
        "Sala empresarial",
        50000,
        4
    )

    # El servicio se almacena en la lista
    servicios.append(sala1)

    print("Servicio de sala creado")
    print(sala1.descripcion())

except ExcepcionServicioInvalido as e:

    print(f"Error en servicio: {e}")

finally:

    print("Finaliza operación 3\n")


# OPERACIÓN 4
# Se crea un servicio de alquiler de equipos
try:

    equipo1 = ServicioEquipo(
        "Video Beam",
        30000,
        2
    )

    servicios.append(equipo1)

    print("Servicio de equipo creado")
    print(equipo1.descripcion())

except ExcepcionServicioInvalido as e:

    print(f"Error en servicio: {e}")

finally:

    print("Finaliza operación 4\n")


# OPERACIÓN 5
# Se crea una asesoría válida
try:

    asesoria1 = ServicioAsesoria(
        "Asesoría en Python",
        80000,
        "intermedio"
    )

    servicios.append(asesoria1)

    print("Servicio de asesoría creado")
    print(asesoria1.descripcion())

except ExcepcionServicioInvalido as e:

    print(f"Error en asesoría: {e}")

finally:

    print("Finaliza operación 5\n")


# OPERACIÓN 6
# Se intenta crear un servicio inválido
try:

    servicio_error = ServicioSala(
        "Sala pequeña",
        -5000,
        2
    )

    servicios.append(servicio_error)

except ExcepcionServicioInvalido as e:

    print(f"Error en servicio: {e}")

finally:

    print("Finaliza operación 6\n")


# OPERACIÓN 7
# Se crea una reserva válida
try:

    reserva1 = Reserva(
        cliente1,
        sala1,
        "15/05/2026",
        4
    )

    # La reserva se guarda en la lista
    reservas.append(reserva1)

    print("Reserva creada correctamente")
    print(reserva1.mostrar_reserva())

except ExcepcionReservaInvalida as e:

    print(f"Error en reserva: {e}")

finally:

    print("Finaliza operación 7\n")


# OPERACIÓN 8
# Se procesa la reserva creada anteriormente
try:

    print(reserva1.procesar_reserva())

except ExcepcionReservaInvalida as e:

    print(f"Error al procesar reserva: {e}")

finally:

    print("Finaliza operación 8\n")


# OPERACIÓN 9
# Se intenta crear una reserva inválida
try:

    reserva_error = Reserva(
        cliente1,
        asesoria1,
        "",
        2
    )

    reservas.append(reserva_error)

except ExcepcionReservaInvalida as e:

    print(f"Error en reserva: {e}")

finally:

    print("Finaliza operación 9\n")


# OPERACIÓN 10
# Se intenta procesar una reserva con un servicio no disponible
try:

    # El servicio cambia su disponibilidad
    equipo1.cambiar_disponibilidad(False)

    reserva2 = Reserva(
        cliente1,
        equipo1,
        "20/05/2026",
        2
    )

    reservas.append(reserva2)

    print(reserva2.procesar_reserva())

except (
    ExcepcionReservaInvalida,
    ExcepcionServicioNoDisponible
) as e:

    print(f"Error del sistema: {e}")

finally:

    print("Finaliza operación 10\n")


# OPERACIÓN 11
# Se calcula el costo de una sala con descuento
try:

    costo_descuento = sala1.calcular_costo(descuento=0.10)

    print("Costo con descuento aplicado:")
    print(costo_descuento)

except Exception as e:

    print(f"Error en cálculo con descuento: {e}")

finally:

    print("Finaliza operación 11\n")


# OPERACIÓN 12
# Se calcula el costo de una asesoría con horas adicionales
try:

    costo_asesoria = asesoria1.calcular_costo(horas=3)

    print("Costo asesoría especializada:")
    print(costo_asesoria)

except Exception as e:

    print(f"Error en cálculo de asesoría: {e}")

finally:

    print("Finaliza operación 12\n")


# OPERACIÓN 13
# Se cancela una reserva existente
try:

    print(reserva1.cancelar_reserva())

except ExcepcionReservaInvalida as e:

    print(f"Error al cancelar reserva: {e}")

finally:

    print("Finaliza operación 13\n")


# OPERACIÓN 14
# Se intenta cancelar nuevamente la misma reserva
try:

    print(reserva1.cancelar_reserva())

except ExcepcionReservaInvalida as e:

    print(f"Error al cancelar reserva: {e}")

finally:

    print("Finaliza operación 14\n")


# OPERACIÓN 15
# Simulación inválida:
# Se intenta crear un cliente con caracteres inválidos
# en el nombre para validar las restricciones del sistema.
try:

    cliente_error = Cliente(
        "Laura123",
        "laura@gmail.com",
        "3204567890"
    )

    clientes.append(cliente_error)

    print(cliente_error.mostrar_informacion())

except ExcepcionClienteInvalido as e:

    print(f"Error en cliente: {e}")

finally:

    print("Finaliza operación 15\n")


# OPERACIÓN 16
# Simulación inválida:
# Se intenta crear una reserva con duración negativa
# para verificar las validaciones de la clase Reserva.
try:

    reserva_invalida = Reserva(
        cliente1,
        sala1,
        "25/05/2026",
        -3
    )

    reservas.append(reserva_invalida)

    print(reserva_invalida.mostrar_reserva())

except ExcepcionReservaInvalida as e:

    print(f"Error en reserva: {e}")

finally:

    print("Finaliza operación 16\n")


# OPERACIÓN 17
# Simulación inválida:
# Se intenta calcular el costo de una asesoría
# utilizando una cantidad de horas inválida.
try:

    costo_invalido = asesoria1.calcular_costo(horas=-2)

    print(costo_invalido)

except Exception as e:

    print(f"Error en asesoría: {e}")

finally:

    print("Finaliza operación 17\n")


# OPERACIÓN 18
# Simulación inválida:
# Se intenta cambiar la disponibilidad del servicio
# usando un valor diferente a booleano.
try:

    sala1.cambiar_disponibilidad("No disponible")

except Exception as e:

    print(f"Error de disponibilidad: {e}")

finally:

    print("Finaliza operación 18\n")


# Registro final de la simulación
registrar_informacion(
    "La simulación del sistema finalizó correctamente"
)

# Mensaje final del sistema
print("FIN DEL SISTEMA")