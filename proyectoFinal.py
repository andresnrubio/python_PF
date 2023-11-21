# --- Proyecto final --- #

# * Primero creamos la base de datos (diccionario)
USUARIOS = {}


# * Definimos una funcion con la que crear un nuevo registro
def registro(BD):
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    BD[usuario] = contraseña
    # TODO Aca deberiamos guardarlo en el archivo


# registro(USUARIOS)

# * Definimos una funcion con la que leer los registros

# print(USUARIOS)

# * Definimos una funcion para guardar el diccionario en un archivo de texto

# * Definimos funcion de login, lee desde archivo, verifica que el usuario exista y posterior que la contraseña sea correcta


# print(registro())

# dict.get("clave a buscar", "error")
