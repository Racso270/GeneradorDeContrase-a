# Generador de Contraseñas Seguras (Versión Final)

## Información del Proyecto
* **Autor:** Oscar Pin
* **Asignatura:** Lógica de Programación
* **Semana:** 8 (Entrega Final)
* **Objetivo:** Software funcional para la generación de claves seguras mitigando riesgos de ciberseguridad.

## Descripción Técnica
Este software ha sido diseñado utilizando **Python**. Se ha implementado una arquitectura modular basada en funciones independientes y el manejo explícito de estructuras de datos para gestionar la información durante la ejecución.

### Estructuras de Datos Utilizadas
1.  **Diccionarios (`dict`):** Se utiliza `MAPA_CARACTERES` para organizar y acceder eficientemente a los conjuntos de caracteres (ASCII, dígitos, puntuación).
2.  **Listas (`list`):**
    * Se utiliza una lista dinámica `historial_sesion` para almacenar temporalmente todas las contraseñas generadas durante la ejecución del programa.
    * Se utilizan listas por comprensión (List Comprehension) para la selección aleatoria de caracteres, optimizando el rendimiento frente a bucles tradicionales.

### Funciones Implementadas
El código se ha refactorizado para cumplir con el principio de responsabilidad única:
* `obtener_pool_caracteres()`: Lógica de concatenación de strings.
* `crear_contrasena_aleatoria()`: Motor de aleatoriedad.
* `guardar_en_historial()`: Gestión de la lista de persistencia temporal.
* `solicitar_entero()` y `solicitar_confirmacion()`: Funciones auxiliares para validación de entradas y manejo de errores (Try/Except).

## Historial de Cambios (Changelog)
**Versión 1.0 (Semana 6-7):**
* Creación inicial con clases (`DataLayer`, `LogicLayer`).
* Funcionalidad básica de generación.

**Versión 2.0 (Semana 8 - Final):**
* **[NUEVO]** Refactorización a Programación Modular (Funciones puras) para mayor legibilidad.
* **[NUEVO]** Implementación de List Comprehensions (Técnica de programación funcional).
* **[NUEVO]** Agregada la función de **Historial de Sesión**, permitiendo al usuario revisar las claves generadas anteriormente mediante el almacenamiento en listas.
* **[MEJORA]** Validación de errores más robusta en funciones separadas.

## Instalación y Uso
1.  Clonar repositorio.
2.  Instalar dependencias: `pip install pyperclip`
3.  Ejecutar: `python generador.py`
