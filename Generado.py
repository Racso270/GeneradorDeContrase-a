import random
import string
# Importamos la librería externa que instalamos (pip install pyperclip)
import pyperclip 

# ==========================================
# SERA LA CAPA 1 DE DATOS (Data Layer)
# Sera la encargafa de proveer los caracteres para la contraseña.
# ==========================================
class DataLayer:
    def obtener_listas_caracteres(self):
        """
        Retorna un diccionario con todos los caracteres disponibles organizados por tipo.
        Usa la librería 'string' nativa de Python.
        """
        return {
            'letras_min': string.ascii_lowercase, # abcdef...
            'letras_may': string.ascii_uppercase, # ABCDEF...
            'numeros': string.digits,             # 0123456789
            'simbolos': string.punctuation        # !#$%&...
        }

# ==========================================
# LA CAPA 2 DE LOGICA DE NEGOCIOS (Business Logic Layer)
# Sera la encargada de generar los caracteres segun se pida
# ==========================================
class LogicLayer:
    def __init__(self):
        # Conectamos la capa lógica con la de datos
        self.datos = DataLayer()
    
    def generar_contrasena(self, longitud, usar_mayus, usar_nums, usar_simb):
        """
        Algoritmo principal para crear la contraseña.
        Recibe: longitud (int) y banderas booleanas (True/False).
        """
        # 1. Siempre iniciamos con letras minúsculas como base
        diccionario = self.datos.obtener_listas_caracteres()
        caracteres_disponibles = diccionario['letras_min']
        
        # 2. Estructuras Lógicas (IF) para añadir complejidad según pida el usuario
        if usar_mayus:
            caracteres_disponibles += diccionario['letras_may']
        if usar_nums:
            caracteres_disponibles += diccionario['numeros']
        if usar_simb:
            caracteres_disponibles += diccionario['simbolos']
            
        contrasena_lista = []
        
        # 3. Estructura Repetitiva (FOR): El corazón del generador
        # Recorre desde 0 hasta la longitud deseada, eligiendo un carácter al azar cada vez.
        for _ in range(longitud):
            caracter_random = random.choice(caracteres_disponibles)
            contrasena_lista.append(caracter_random)
            
        # Convertimos la lista en un texto simple (string)
        return "".join(contrasena_lista)

    def copiar_portapapeles(self, texto):
        """Intenta copiar el texto al sistema operativo."""
        try:
            pyperclip.copy(texto)
            return True
        except Exception:
            return False

# ==========================================
# LA CAPA 3 DE PRESENTACIÓN (User Interface)
# Se encarga de hablar con el humano (Inputs y Prints).
# ==========================================
def main():
    logica = LogicLayer()
    
    print("\n" + "="*40)
    print("   SISTEMA GENERADOR DE CONTRASEÑAS")
    print("   (Arquitectura de 3 Capas)")
    print("="*40 + "\n")
    
    # --- Validación de Entrada (Estructura Repetitiva WHILE) ---
    # Este bucle no se rompe hasta que el usuario ingrese un número válido.
    while True:
        try:
            entrada = input(">> Ingrese la longitud de la contraseña (ej. 12): ")
            longitud = int(entrada) # Intentamos convertir a entero
            
            # Estructura Lógica (IF) para validar que sea positivo
            if longitud > 0:
                break # Salimos del bucle si todo está bien
            else:
                print("   [!] Error: El número debe ser mayor a 0.")
        except ValueError:
            print("   [!] Error: Por favor ingrese solo números.")

    # --- Captura de Opciones ---
    print("\nConfigure sus parámetros (escriba 's' para sí, cualquier otra tecla para no):")
    mayus = input("   ¿Incluir Mayúsculas? ").lower() == 's'
    nums  = input("   ¿Incluir Números?    ").lower() == 's'
    simb  = input("   ¿Incluir Símbolos?   ").lower() == 's'
    
    # --- Ejecución ---
    resultado = logica.generar_contrasena(longitud, mayus, nums, simb)
    
    print("\n" + "-"*40)
    print(f"CONTRASEÑA GENERADA:  {resultado}")
    print("-"*40)
    
    # --- Opción Extra ---
    if input("\n>> ¿Copiar al portapapeles? (s/n): ").lower() == 's':
        logica.copiar_portapapeles(resultado)
        print("   [OK] ¡Copiado exitosamente!")
    
    input("\nPresione ENTER para salir...")

# Punto de entrada del programa
if __name__ == "__main__":
    main()