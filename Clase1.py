'''
Apuntes Python Clase 1
'''
# -----------------------------------------------------------------------------
# 📌 TIPOS NUMÉRICOS EN PYTHON
# -----------------------------------------------------------------------------

'''
Enteros (int)
    Los enteros son números sin decimales, pueden ser positivos o negativos.
'''
numero_entero = 42
numero_negativo = -10
print("Número entero:", numero_entero)
print("Número negativo:", numero_negativo)
print("Tipo de dato:", type(numero_entero))  # <class 'int'>


'''
Decimales (float)
    Los números flotantes son aquellos que tienen decimales.
'''
numero_decimal = 3.14159
temperatura = -12.5
print("Número decimal:", numero_decimal)
print("Temperatura:", temperatura)
print("Tipo de dato:", type(numero_decimal))  # <class 'float'>

'''
Números complejos (complex)
    Los números complejos tienen una parte real y una imaginaria (se usa "j").
'''
num_complejo = 2 + 3j
print("Número complejo:", num_complejo)
print("Parte real:", num_complejo.real, "| Parte imaginaria:", num_complejo.imag)
print("Tipo de dato:", type(num_complejo))  # <class 'complex'>

'''
Operaciones matemáticas básicas con números
'''
suma = 10 + 5
resta = 10 - 3
multiplicacion = 4 * 2
division = 10 / 3  # Siempre devuelve un float
division_entera = 10 // 3  # División sin decimales
modulo = 10 % 3  # Resto de la división
potencia = 2 ** 3  # Exponente (2 elevado a 3)

print("\nOperaciones matemáticas:")
print("Suma:", suma, "| Resta:", resta, "| Multiplicación:", multiplicacion)
print("División:", division, "| División entera:", division_entera)
print("Módulo:", modulo, "| Potencia:", potencia)


# -----------------------------------------------------------------------------
# 📌 BOOLEANOS (bool)
# -----------------------------------------------------------------------------
'''
Un booleano solo puede tener dos valores: True (verdadero) o False (falso)
'''
es_python_facil = True
es_python_dificil = False

print("\nBooleanos:")
print("Es Python fácil?", es_python_facil)
print("Es Python difícil?", es_python_dificil)

'''
Comparaciones que devuelven valores booleanos
'''
mayor_que = 10 > 5  # True porque 10 es mayor que 5
menor_que = 10 < 5  # False porque 10 no es menor que 5
igualdad = 10 == 10  # True porque ambos son iguales
diferente = 10 != 5  # True porque 10 y 5 son distintos

print("10 es mayor que 5:", mayor_que)
print("10 es menor que 5:", menor_que)
print("10 es igual a 10:", igualdad)
print("10 es distinto de 5:", diferente)

'''
Operaciones lógicas con booleanos
'''
and_logico = True and False  # False porque ambos deben ser True
or_logico = True or False  # True porque al menos uno es True
not_logico = not True  # False porque invierte el valor

print("\nOperaciones lógicas:")
print("True AND False:", and_logico)
print("True OR False:", or_logico)
print("NOT True:", not_logico)


# -----------------------------------------------------------------------------
# 📌 3️⃣ CADENAS DE TEXTO (str)
# -----------------------------------------------------------------------------
'''
Una cadena de texto es una secuencia de caracteres delimitados por comillas
'''
texto_simple = "Hola, mundo"
texto_doble = 'Python es genial'

print("\nCadenas de texto:")
print("Texto simple:", texto_simple)
print("Texto doble:", texto_doble)

'''
Concatenación de cadenas (unir textos)
'''
mensaje = "Python" + " es " + "increíble"
print("Concatenación de cadenas:", mensaje)

'''
Repetición de cadenas
'''
repetida = "Python! " * 3
print("Repetición de cadenas:", repetida)

'''
Acceder a caracteres de una cadena usando índices
'''
palabra = "Python"
primera_letra = palabra[0]  # Primer carácter (P)
ultima_letra = palabra[-1]  # Último carácter (n)

print("\nAcceso a caracteres:")
print("Primera letra:", primera_letra)
print("Última letra:", ultima_letra)

'''
Slicing (extraer partes de una cadena)
'''
subcadena = palabra[0:3]  # Obtiene 'Pyt'
print("Subcadena:", subcadena)

'''
Métodos útiles para cadenas
'''
mayusculas = palabra.upper()  # Convierte en mayúsculas
minusculas = palabra.lower()  # Convierte en minúsculas
longitud = len(palabra)  # Devuelve la cantidad de caracteres

print("\nMétodos de cadenas:")
print("Mayúsculas:", mayusculas)
print("Minúsculas:", minusculas)
print("Longitud de la palabra:", longitud)
