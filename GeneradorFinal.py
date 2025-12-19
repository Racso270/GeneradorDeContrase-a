import random
import string
import pyperclip

# --- ESTRUCTURAS DE DATOS GLOBALES ---
# Diccionario para mapear los tipos de caracteres
MAPA_CARACTERES = {
    'mayus': string.ascii_uppercase,
    'nums': string.digits,
    'simb': string.punctuation
}

# Lista para almacenar el historial de contraseñas de esta sesión
historial_sesion = []

# --- FUNCIONES (PROGRAMACIÓN MODULAR) ---

def obtener_pool_caracteres(usar_mayus, usar_nums, usar_simb):
    """
    Crea y retorna la cadena completa de caracteres disponibles
    basado en las decisiones del usuario.
    """
    # Estructura base: siempre minúsculas
    pool = string.ascii_lowercase
    
    # Lógica condicional para agregar conjuntos del diccionario
    if usar_mayus:
        pool += MAPA_CARACTERES['mayus']
    if usar_nums:
        pool += MAPA_CARACTERES['nums']
    if usar_simb:
        pool += MAPA_CARACTERES['simb']
    
    return pool

def crear_contrasena_aleatoria(longitud, pool_caracteres):
    """
    Aplica programación funcional (list comprehension) para generar
    la contraseña aleatoria.
    """
    # Uso de List Comprehension (Estructura eficiente)
    lista_caracteres = [random.choice(pool_caracteres) for _ in range(longitud)]
    return "".join(lista_caracteres)

def guardar_en_historial(contrasena):
    """
    Agrega la contraseña generada a la estructura de datos (lista).
    """
    historial_sesion.append(contrasena)

def mostrar_historial():
    """
    Recorre e imprime la lista de contraseñas generadas.
    """
    if not historial_sesion:
        print("\n[!] Aún no hay historial.")
        return

    print("\n" + "*"*30)
    print("   HISTORIAL DE SESIÓN")
    print("*"*30)
    for i, pwd in enumerate(historial_sesion, 1):
        print(f" {i}. {pwd}")
    print("*"*30)

def solicitar_entero(mensaje):
    """Validación robusta de entrada numérica."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("   [!] Debe ser mayor a 0.")
        except ValueError:
            print("   [!] Ingrese solo números.")

def solicitar_confirmacion(mensaje):
    """Retorna True si el usuario escribe 's'."""
    return input(mensaje).lower() == 's'

# --- FUNCIÓN PRINCIPAL ---
def main():
    print("=== GENERADOR DE CONTRASEÑAS MEJORADO ===")
    
    while True:
        # 1. Entradas
        longitud = solicitar_entero("\n>> Longitud de contraseña: ")
        mayus = solicitar_confirmacion("   ¿Incluir Mayúsculas? (s/n): ")
        nums = solicitar_confirmacion("   ¿Incluir Números?    (s/n): ")
        simb = solicitar_confirmacion("   ¿Incluir Símbolos?   (s/n): ")

        # 2. Procesamiento
        pool = obtener_pool_caracteres(mayus, nums, simb)
        password = crear_contrasena_aleatoria(longitud, pool)
        
        # 3. Guardado en estructura de datos
        guardar_en_historial(password)

        # 4. Salida
        print(f"\n---> CONTRASEÑA: {password}")

        # 5. Funcionalidades extra
        if solicitar_confirmacion("\n>> ¿Copiar al portapapeles? (s/n): "):
            pyperclip.copy(password)
            print("   [Copiado!]")
        
        if solicitar_confirmacion(">> ¿Ver historial de sesión? (s/n): "):
            mostrar_historial()

        if not solicitar_confirmacion("\n>> ¿Generar otra? (s/n para salir): "):
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()