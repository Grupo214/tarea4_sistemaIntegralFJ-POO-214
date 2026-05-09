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

print("SOFTWARE FJ\n") # Mensaje inicial del sistema


# OPERACIÓN 1
# Se intenta crear un cliente válido
try:

    cliente1 = Cliente(
        "Laura Medina",
        "laura.medina@gmail.com",
        "3204567812"
    )

    
    clientes.append(cliente1) # Se guarda el cliente en la lista

    print("Cliente registrado correctamente")
    print(cliente1.mostrar_informacion())

except ExcepcionClienteInvalido as e:

    print(f"Error en cliente: {e}") # Se muestra el error si los datos son inválidos

finally:

    print("Finaliza operación 1\n") # Mensaje final de la operación


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

    
    servicios.append(sala1) # El servicio se almacena en la lista

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

    reservas.append(reserva1) # La reserva se guarda en la lista

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

    equipo1.cambiar_disponibilidad(False) # El servicio cambia su disponibilidad

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

registrar_informacion(     # Se registra el final de la simulación en el archivo log
    "La simulación del sistema finalizó correctamente"
)

print( "FIN DEL SISTEMA") # Mensaje final del sistema