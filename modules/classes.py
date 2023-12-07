class Client:
    def __init__(self, name, lastname, personalId, phone, emailAddress):
        self.name = name
        self.lastname = lastname
        self.__personalId = personalId
        self.__phone = phone
        self.__emailAddress = emailAddress
        self.interest = ["movies", "series", "games"]

    def __str__(self):
        return f"El cliente es {self.name} {self.lastname}, con identificacion: {self.__personalId}"

    def contact_info(self):
        return f"Contacto: {self.__phone}, {self.__emailAddress}"

    def get_interest(self):
        # Ver lo que indico el profesor para reformular los metodos de listas
        return f"{self.interest}"

    def add_interest(self, new_interest):
        pass

    def delete_interest(self, interest_to_delete):
        pass
