# Checkpoint 3
# Exercise 1: Create a variable of each type: string, integer, list, boolean.

nombre_usuario = "Carolina"     #String
radio_circulo = 20              #Integer
lista_invitados = ['Juan', 'Antonio', 'Luisa', 'Maria']     #List
acceso_concedido = False        #Boolean


# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable.

tres_primeras_letras = nombre_usuario[0:3]
print(tres_primeras_letras)  # Output: Car


# Exercise 3: Use an index to grab the first element from your list.

primer_elemento= lista_invitados[0]
print(primer_elemento)  # Output: Juan


# Exercise 4: Create a new number variable that adds 10 to your original number.

radio_incrementado = radio_circulo + 10
print(radio_incrementado)  # Output: 30


# Exercise 5: Use an index to get the last element in your list.

ultimo_elemento = lista_invitados[-1]
print(ultimo_elemento)  # Output: Maria


# Exercise 6: Use split to transform the following string into a list.

names = 'harry,alex,susie,jared,gail,conner'
lista_nombre = names.split(',')
print(lista_nombre)  # Output: ['harry', 'alex', 'susie', 'jared', 'gail', 'conner']


# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase.
# Create a new string that takes the uppercase word and the rest of the original string.

primer_nombre = names[0:5]  # 'harry'
nombre_mayusculas = primer_nombre.upper()  # 'HARRY'
new_string = nombre_mayusculas + names[5:]
print(new_string)  # Output: HARRY,alex,susie,jared,gail,conner



# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.

mensaje = f"El radio del círculo es {radio_circulo}."
print(mensaje)  # Output: El radio del círculo es 20


# Exercise 9: Print “hello world”.

print("hello world")  # Output: hello world


#Exercise 10
'''
Además necesito que me crees una cadena que contenga la palabra "Hola".
Usando la palabra clave en el método de búsqueda o el índice, busque y seleccione "Hola" en su cadena.
Y usando la función de reemplazo, reemplace "Hola" en su cadena con "adiós".
Este ejercicio de Python debes subirlo a tu Git-Hub o Replit para poder revisarlo
'''
saludo = 'Hola, buenos días. Qué hora es?'
print(saludo.index('Hola'))  # Encuentra la posición de 'Hola' en la cadena e muestra su posición dentro del string
saludo = saludo.replace('Hola', 'adiós')
print(saludo)  # Output: adiós, buenos días. Qué hora es?
