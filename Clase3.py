# 🔹 Longitud de una cadena (len)
  # Podemos medir cuántos caracteres tiene una cadena usando len().
  # Útil para validar el tamaño de una contraseña o contar caracteres.

nombre = "Mario Flores"
print("Longitud del nombre:", len(nombre))

# 🔹 Convertir texto a mayúsculas y minúsculas
  # Métodos upper() y lower().
  # Útil para normalizar datos.

print("En mayúsculas:", nombre.upper())
print("En minúsculas:", nombre.lower())

# 🔹 Extraer parte de una cadena (Slicing)
  # Podemos seleccionar solo una parte del texto.
  # Se usa en procesamiento de texto.

print("Primeros 3 caracteres:", nombre[:3])  # "Mar"
print("Últimos 4 caracteres:", nombre[-4:])  # "ores"

# 🔹 Reemplazar palabras en una cadena
  # Métod replace(), cambia palabras dentro de un texto.
  # Útil en limpieza de datos.

frase = "Me gusta Java"
print("Cambio de palabra:", frase.replace("Java", "Python"))

# 🔹 Verificar si una cadena contiene otra (in)
  # Podemos comprobar si una palabra está dentro de otra.
  # Se usa en búsquedas.

print("Python" in frase)  # False
nueva_frase = "Me gusta Python"
print("Python" in nueva_frase)  # True

# 🔹 Unir varias palabras en una sola cadena
  # Métod join() para unir listas en una sola cadena.
  # Se usa en generación de texto dinámico.

palabras = ["Hola", "mundo", "Python"]
print("Frase completa:", " ".join(palabras))

# 🔹 Dividir una cadena en partes
  # Métod split() para separar una cadena en una lista.
  # Útil en procesamiento de archivos de texto.

oracion = "Python es divertido"
palabras = oracion.split()  # ["Python", "es", "divertido"]

print("Lista de palabras:", palabras)

# 🔹 Redondear un número decimal
  # Métod round(), redondea números flotantes.
  # Usado en cálculos financieros.

numero = 3.14159
print("Número redondeado:", round(numero, 2))  # 3.14


# 🔹 Formatear números con decimales
  # Métod format() para mostrar un número con decimales fijos.
  # Se usa en reportes y facturas.

precio = 19.99
print("Precio con 2 decimales: {:.2f}".format(precio))  # "19.99"


# 🔹 Obtener el valor ASCII de un carácter
  # Función ord() devuelve el valor ASCII.
  # Se usa en criptografía.

print("Código ASCII de 'A':", ord('A'))  # 65


# 🔹 Elevar un número al cuadrado
  # Operador ** para calcular potencias.
  # Se usa en matemáticas.

numero = 5
print("5 elevado al cuadrado:", numero ** 2)  # 25


# 🔹 Obtener la raíz cuadrada
  # Usamos ** (1/2) para calcular la raíz cuadrada.
  # Alternativa a la función sqrt().

print("Raíz cuadrada de 25:", 25 ** 0.5)  # 5.0


# 🔹 División entera y resto
  # División normal /, entera // y módulo %.
  # Útil para cálculos matemáticos.

print("División normal:", 10 / 3)  # 3.3333
print("División entera:", 10 // 3)  # 3
print("Resto:", 10 % 3)  # 1

# 🔹 Generar un número aleatorio
  # random.randint() genera números aleatorios.
  # Se usa en juegos y simulaciones.

import random

print("Número aleatorio entre 1 y 10:", random.randint(1, 10))


# 🔹 Convertir números a cadenas y viceversa
  # str() convierte un número a texto, int() convierte texto a número.
  # Útil para manipulación de datos.

numero = 100
texto = str(numero)  # "100"
print("Convertido a texto:", texto)

cadena = "200"
numero = int(cadena)  # 200
print("Convertido a número:", numero)


# 🔹 Redondear siempre hacia arriba
  # Usamos math.ceil().
  # Se usa en cálculos financieros.

import math
print("Redondeo hacia arriba de 3.2:", math.ceil(3.2))  # 4


# 🔹 Convertir una lista en un conjunto (eliminar duplicados)
  # set() convierte listas en conjuntos.
  # Se usa en análisis de datos.

numeros = [1, 2, 2, 3, 4, 4, 5]
sin_duplicados = set(numeros)
print("Lista sin duplicados:", sin_duplicados)


# 🔹 Repetir una cadena varias veces
  # * multiplica cadenas.
  # Se usa en generación de texto dinámico.

print("Python! " * 3)


# 🔹 Obtener el tipo de una variable
  # type() nos dice el tipo de dato.
  # Útil para depuración.

dato = 3.14
print("Tipo de dato:", type(dato))  # <class 'float'>


# 🔹 Combinar cadenas y variables en un print
  # Usamos f"" para incluir variables dentro de un texto.
  # Se usa en generación de mensajes dinámicos.

nombre = "Mario"
edad = 30
print(f"Hola, soy {nombre} y tengo {edad} años.")

# 📌 IMPORTANTE
# La f dentro del print() indica que estamos utilizando una f-string o formatted string literals, una forma moderna y eficiente de formatear cadenas en Python.
# 🔹 ¿Qué es una f-string?
  # Una f-string (f"") permite insertar variables y expresiones directamente dentro de una cadena de texto, sin necesidad de concatenaciones (+) o métodos como .format().
# Ejemplo sin f-string (concatenación tradicional):
nombre = "Mario"
edad = 30
print("Hola, soy " + nombre + " y tengo " + str(edad) + " años.")

# 🔹 Inconvenientes:
   # Se deben concatenar cadenas con +.
   # Se necesita convertir edad a str(), ya que no se pueden concatenar strings y números directamente.

# 🔹 Ejemplo con f-string (forma más moderna y legible):
nombre = "Mario"
edad = 30
print(f"Hola, soy {nombre} y tengo {edad} años.")

# 🔹 Ventajas:
   # Más legible y fácil de escribir.
   # No requiere convertir números a cadenas (str()).
   # Se pueden incluir expresiones dentro de {}.

# 📌 Aplicación en tu código
numero = float(input("Escribe un número decimal: "))

print(f"Número redondeado: {round(numero, 2)}")  # Inserta el número redondeado
print(f"Cuadrado: {numero ** 2}")  # Calcula y muestra el cuadrado
print(f"Raíz cuadrada: {numero ** 0.5}")  # Calcula y muestra la raíz cuadrada

# 🔹 ¿Por qué se usa f"" en este caso?
   #  Porque permite insertar directamente los resultados de round(numero, 2), numero ** 2 y numero ** 0.5 dentro del texto sin concatenaciones.

# 📌 ¿Puedo hacer lo mismo sin f-strings?
# Sí, pero sería menos intuitivo:

print("Número redondeado: " + str(round(numero, 2)))
print("Cuadrado: " + str(numero ** 2))
print("Raíz cuadrada: " + str(numero ** 0.5))

# 🔴 Problemas:
   # Necesitas usar str() para convertir valores numéricos en texto.
   # Más código y más propenso a errores.

# 💡 Conclusión: Usa f-strings siempre que necesites incluir variables dentro de cadenas. Son más eficientes, legibles y recomendadas en Python moderno.