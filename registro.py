import datetime# Se importa datatime para trabajar con la fecha y hora actual
import os#Se importa os para poder crear los archivos si no existen

# Clase para manejar el registro de eventos y errores del sistema
class Registro:
    
    def __init__(self, nombre_archivo="registro_sistema.txt"):# Inicializa el registro con un archivo específico
        self.nombre_archivo = nombre_archivo#Nombre del archivo donde se registran los eventos
        self._crear_archivo_si_no_existe()
    
    def _crear_archivo_si_no_existe(self):
        # Crea el archivo de registro si este no existe
        if not os.path.exists(self.nombre_archivo):
            with open(self.nombre_archivo, "w") as archivo:
                archivo.write("=== INICIO DEL SISTEMA ===\n")
                archivo.write(f"Fecha: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")#Se convierte la fecha a un formatos legible dia-mes-año| hora:min:seg
                archivo.write("=" * 50 + "\n\n")
    
    def _obtener_marca_tiempo(self):
        # Retorna la fecha y hora actual formateada
        return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    def registrar_informacion(self, mensaje):
        # Registra un mensaje informativo
        self._escribir_registro("INFO", mensaje)
    
    def registrar_error(self, mensaje, excepcion=None):
        # Registra un error
        if excepcion:
            mensaje_completo = f"{mensaje} | Excepción: {type(excepcion).__name__}: {str(excepcion)}"#Descripción del error
        else:
            mensaje_completo = mensaje
        self._escribir_registro("ERROR", mensaje_completo)
    
    def registrar_advertencia(self, mensaje):
        # Registra una advertencia
        self._escribir_registro("ADVERTENCIA", mensaje)
    
    def registrar_exito(self, mensaje):
        # Registra una operacion exitosa
        self._escribir_registro("ÉXITO", mensaje)
    
    def _escribir_registro(self, tipo, mensaje):# Se escribe en archivo de registro
        
        try:
            marca_tiempo = self._obtener_marca_tiempo()
            linea = f"[{marca_tiempo}] {tipo}: {mensaje}\n"
            
            with open(self.nombre_archivo, "a") as archivo:
                archivo.write(linea)
        except IOError as e:
            # Si falla la escritura, se imprime en consola
            print(f"Error al escribir en registro: {e}")
            print(f"Mensaje no registrado: [{tipo}] {mensaje}")
    
    def obtener_contenido_registro(self):
        # Retorna el contenido actual del archivo de registro
        try:
            with open(self.nombre_archivo, "r") as archivo:
                return archivo.read()
        except FileNotFoundError:
            return "Archivo de registro no encontrado"
    
    def limpiar_registro(self):
        # Limpia el contenido del archivo de registro 
        try:
            with open(self.nombre_archivo, "w") as archivo:
                archivo.write("=== REGISTRO LIMPIADO ===\n")
            self.registrar_informacion("Archivo de registro limpiado manualmente")
        except IOError as e:
            print(f"Error al limpiar registro: {e}")


# Instancia global del registro 
registro_global = Registro()

# Funciones de conveniencia para uso rápido
def registrar(tipo, mensaje):
    # Función simplificada para registrar eventos
    registro_global._escribir_registro(tipo, mensaje)

def registrar_error(mensaje, excepcion=None):
    # Registra un error de forma rapida
    registro_global.registrar_error(mensaje, excepcion)

def registrar_informacion(mensaje):
    # Registra información de forma rapida
    registro_global.registrar_informacion(mensaje)

def registrar_advertencia(mensaje):
    # Registra una advertencia de forma rapida
    registro_global.registrar_advertencia(mensaje)
