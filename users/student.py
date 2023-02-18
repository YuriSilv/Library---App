class student:
    def __init__(self, name: str, date_of_birth: str, adress: str, cpf: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.adress = adress
        self.cpf = cpf

    def __str__(self):
        print("Name: ", self.name)
        print("Date of birth: ", self.date_of_birth)
        print("Adress: ", self.adress)
        print("CPF: ", self.cpf)