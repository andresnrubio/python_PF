class Cliente:
    def __init__(self, name, lastname, personalId, phone, emailAddress):
        self.name = name
        self.lastname = lastname
        self.__personalId = personalId
        self.__phone = phone
        self.__emailAddress = emailAddress

    def __str__(self):
        return f"El cliente es {self.name} {self.lastname}, con identificacion: {self.__personalId}"

    def contact_Info(self):
        return f"Contacto: {self.__phone}, {self.__emailAddress}"


cliente_1 = Cliente("Andres", "Rubio", 123456, 11544564631, "andres@Rubio.com")

print(cliente_1)
print(cliente_1.contact_Info())
