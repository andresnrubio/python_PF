# --- Proyecto final --- #

# * Primero creamos la base de datos (diccionario)
USERS = {}


# * Definimos una funcion con la que crear un nuevo registro
def register(BD):
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    BD[usuario] = contraseña
    saveUsers(BD)


# * Definimos una funcion para guardar el diccionario en un archivo de texto
def saveUsers(data):
    users = open("users.txt", "w")
    users.write(str(data))
    users.close()


# * Definimos una funcion con la que leer los registros


def readUsersDB():
    users = open("users.txt", "r")
    usersData = users.read()
    users.close()
    return usersData


# * Definimos funcion de login, verifica que el usuario exista y posterior que la contraseña sea correcta


def login(BD):
    user = input("Ingrese su nombre de usuario: ")
    if user in BD:
        password = input("Ingrese su contraseña: ")
        if BD[user] == password:
            print("Inicio de sesion exitoso")
        else:
            print("Contraseña incorrecta")

    else:
        print("El usuario es inexistente")


# Ejecucion

register(USERS)

print(readUsersDB())

login(USERS)
