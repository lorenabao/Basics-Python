# /*
#  * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
#  * - Recuerda que todas las instrucciones de participación están en el
#  *   repositorio de GitHub.
#  *
#  * Lo primero... ¿Ya has elegido un lenguaje?
#  * - No todos son iguales, pero sus fundamentos suelen ser comunes.
#  * - Este primer reto te servirá para familiarizarte con la forma de participar
#  *   enviando tus propias soluciones.
#  *
#  * EJERCICIO:
#  * - Crea un comentario en el código y coloca la URL del sitio web oficial del
#  *   lenguaje de programación que has seleccionado.
#  * - Representa las diferentes sintaxis que existen de crear comentarios
#  *   en el lenguaje (en una línea, varias...).
#  * - Crea una variable (y una constante si el lenguaje lo soporta).
#  * - Crea variables representando todos los tipos de datos primitivos
#  *   del lenguaje (cadenas de texto, enteros, booleanos...).
#  * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
#  *
#  * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
#  * debemos comenzar por el principio.
#  */

# https://es.python.org/

### Variables ###

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

# Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)

# Cambiamos su tipo
name = 35
age = "Brais"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))
